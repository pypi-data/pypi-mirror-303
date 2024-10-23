import gzip
import re
import sys
import zipfile

from dataclasses import dataclass, fields, KW_ONLY
from http.client import HTTPResponse
from mimetypes import guess_extension
from pathlib import Path
from struct import pack
from urllib.parse import ParseResult, urlparse
from uuid import uuid4

from lxml import etree

from .loadmetadata import load_metadata
from .packagedata import PackageData
from ..scrapers import scrape

_CONTENT_DIR = 'Content'
_SUPPORT_DIR = 'Runtime/Support'

_USER_FACING_DAZ_EXTENSIONS = ('.daz', '.djl', '.duf', '.ds', '.dsa', '.dsb', '.dse')
_OTHER_DAZ_EXTENSIONS = ('.dhdm', '.dsd', '.dsf', '.dsj', '.dso', '.dsv')
_COMPRESSABLE_DAZ_EXTENSIONS = ('.dsf', '.duf')
_NON_USER_FACING_DIRECTORIES = ('data', "readme's", 'runtime', 'uninstallers')

_USER_FACING_POSER_EXTENSIONS = ('.pz3', '.pzz', '.cr2', '.crz', '.pz2', '.p2z', '.fc2', '.fcz', '.hr2', '.hrz', '.hd2', '.hdz', '.pp2', '.ppz', '.lt2', '.ltz', '.cm2', '.cmz', '.mc6', '.mcz', '.mt5', '.mz5')
_OTHER_POSER_EXTENSIONS = ('.pmd',)
_POSER_USER_FACING_DIRECTORIES = ('camera', 'character', 'collections', 'face', 'hair', 'hand', 'light', 'materials', 'pose', 'props', 'scene')

_EXCLUDE_FILES = tuple(x.lower() for x in ('.DS_Store', '._.DS_Store', 'InstallManagerFileRegister.json', 'Desktop.ini', 'pspbrwse.jbf', 'Thumbs.db'))
_EXCLUDE_SUFFIXES = ('.xmp', '.bak')


# DIM does not support Unicode filenames in ZIP files due to using the minizip 1.01 library.
# Examining official DAZ packages reveals Windows-1252 encoding is used. Packages with
# filenames using non ASCII characters may not extract correctly on OS X.
Ascii_ZipInfo = zipfile.ZipInfo
class Windows1252_ZipInfo(zipfile.ZipInfo):
	def _encodeFilenameFlags(self):
		try:
			return self.filename.encode('Windows-1252'), self.flag_bits
		except UnicodeEncodeError as e:
			raise SystemExit(f'DIM does not support Unicode filenames: {self.filename}') from e

	def __init__(self, filename: str = "NoName", date_time: tuple[int, int, int, int, int, int] = (1980,1,1,0,0,0)):
		super().__init__(filename, date_time)

		# Encode non ASCII filenames as Windows-1252, but also add unicode filename field for non DIM tools to extract
		if self.filename.encode() != self.filename.encode('Windows-1252', 'replace'):
			UNICODE_PATH_EXTRA_FIELD_ID = 0x7075
			encoded_filename = self.filename.encode()
			crc = zipfile.crc32(self._encodeFilenameFlags()[0])	# pyright: ignore[reportAttributeAccessIssue, reportUnknownMemberType, reportUnknownVariableType]
			self.extra += pack(f'<HHBL{len(encoded_filename)}s', UNICODE_PATH_EXTRA_FIELD_ID, len(encoded_filename) + 5, 1, crc, encoded_filename)

@dataclass
class PackageGenerator(PackageData):
	id: int | None = None
	url: ParseResult | None = None
	verbose: bool = False
	_: KW_ONLY
	content_location: Path

	@property
	def sanitized_name(self) -> str:
		alpha_numeric_regex = re.compile(r'[^0-9A-Za-z]')
		return alpha_numeric_regex.sub('', self.name or '')

	@property
	def zip_filename(self) -> str:
		# Max SKU length for filename is 8 characters, but can be longer in metadata
		# Overflow SKU into source prefix if space is available as SKU will be incorrect
		# in DIM either way, and DIM does not allow filtering by source prefix
		sku = f'{self.sku:08}'[-8:]
		prefix = f'{self.prefix}{str(self.sku)[:-8][:7 - len(self.prefix or '')]}'
		return f"{prefix}{sku}{f'-{self.id:02}' if self.id else ''}_{self.sanitized_name}.zip"

	@property
	def metadata_filename_base(self) -> str:
		# NOTE: This is a guess and may need to be expanded with additional characters
		_REPLACE_METADATA_FILENAME_CHARACTERS = r'[\\/*?:"<>|!. ]'
		return re.sub(_REPLACE_METADATA_FILENAME_CHARACTERS, '_', f"{self.store}_{self.sku}_{self.name}")

	@property
	def metadata_image_extension(self) -> str | None:
		extension = None

		if isinstance(self.image, Path):
			extension = self.image.suffix
		elif isinstance(self.image, HTTPResponse) and self.image:
			if 'Content-Type' in self.image.info():
				# strict=False because ShareCG specifies incorrect MIME type for JPEG.
				if ext := guess_extension(self.image.info()['Content-Type'], False):
					extension = ext
			else:
				extension = Path(urlparse(self.image.url).path).suffix

		return extension if extension in ['.jpg', '.png'] else None

	@property
	def manifest_file(self) -> bytes:
		if self.verbose:
			print('Generating Manifest')

		manifest = etree.Element('DAZInstallManifest', VERSION='0.1')
		etree.SubElement(manifest, 'GlobalID', VALUE=str(self.global_id))

		for _, relative_file_path in self._files():
			etree.SubElement(manifest, 'File', TARGET='Content', ACTION='Install', VALUE=(_CONTENT_DIR / relative_file_path).as_posix())

		etree.SubElement(manifest, 'File', TARGET='Content', ACTION='Install', VALUE=f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}.dsa')
		etree.SubElement(manifest, 'File', TARGET='Content', ACTION='Install', VALUE=f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}.dsx')
		if image_extension := self.metadata_image_extension:
			etree.SubElement(manifest, 'File', TARGET='Content', ACTION='Install', VALUE=f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}{image_extension}')

		etree.indent(manifest, space=' ')
		return etree.tostring(manifest, encoding='UTF-8', pretty_print=True)

	@property
	def supplement_file(self) -> bytes:
		if self.verbose:
			print('Generating Supplement')

		if not self.name:
			raise RuntimeError('Missing Product Name')

		supplement = etree.Element('ProductSupplement', VERSION='0.1')
		etree.SubElement(supplement, 'ProductName', VALUE=self.name)
		etree.SubElement(supplement, 'InstallTypes', VALUE='Content')
		etree.SubElement(supplement, 'ProductTags', VALUE=','.join(sorted(self.tags)))

		etree.indent(supplement, space=' ')
		return etree.tostring(supplement, encoding='UTF-8', pretty_print=True)

	@property
	def metadata_file(self) -> bytes:
		if self.verbose:
			print('Generating Metadata')

		if not self.name:
			raise RuntimeError('Missing Product Name')

		metadata = etree.Element('ContentDBInstall', VERSION='1.0')
		product = etree.SubElement(etree.SubElement(metadata, 'Products'), 'Product', VALUE=self.name)

		if self.store:
			etree.SubElement(product, 'StoreID', VALUE=self.store)

		if self.global_id:
			etree.SubElement(product, 'GlobalID', VALUE=str(self.global_id))

		if self.sku:
			etree.SubElement(product, 'ProductToken', VALUE=str(self.sku))

		if self.description:
			etree.SubElement(product, 'Description').text=etree.CDATA(self.description)

		if self.artists:
			artists = etree.SubElement(product, 'Artists')
			for artist in self.artists:
				etree.SubElement(artists, 'Artist', VALUE=artist)

		# Assets / SupportAssets
		assets = etree.SubElement(product, 'Assets')
		support_assets = etree.SubElement(product, 'SupportAssets', VALUE=f'/{_SUPPORT_DIR}/{self.metadata_filename_base}.dsx')
		for _, relative_file_path, in self._files():
			suffix = relative_file_path.suffix.lower()
			path_parts = [p.lower() for p in relative_file_path.parts]
			if ((suffix in _USER_FACING_DAZ_EXTENSIONS and path_parts[0] not in _NON_USER_FACING_DIRECTORIES) or
				(suffix in _USER_FACING_DAZ_EXTENSIONS + _USER_FACING_POSER_EXTENSIONS and len(path_parts) > 3 and
	 			path_parts[0] == 'runtime' and path_parts[1] == 'libraries' and path_parts[2] in _POSER_USER_FACING_DIRECTORIES)):

				asset_path = relative_file_path.as_posix()
				asset = etree.SubElement(assets, 'Asset', VALUE=asset_path)

				if self.assets and asset_path in self.assets:
					asset_data = self.assets[asset_path]
					if asset_data.description:
						etree.SubElement(asset, 'Description').text=etree.CDATA(asset_data.description)

					if asset_data.content_type:
						etree.SubElement(asset, 'ContentType', VALUE=asset_data.content_type)

					if asset_data.audience:
						etree.SubElement(asset, 'Audience', VALUE=asset_data.audience)

					if asset_data.categories and len(asset_data.categories):
						categories = etree.SubElement(asset, 'Categories')
						for category in asset_data.categories:
							etree.SubElement(categories, 'Category', VALUE=category)

					if asset_data.tags and len(asset_data.tags):
						tags = etree.SubElement(asset, 'Tags')
						for tag in asset_data.tags:
							etree.SubElement(tags, 'Tag', VALUE=tag)

					if asset_data.compatibilities and len(asset_data.compatibilities):
						compatibilities = etree.SubElement(asset, 'Compatibilities')
						for compatibility in asset_data.compatibilities:
							etree.SubElement(compatibilities, 'Compatibility', VALUE=compatibility)

					if asset_data.compatibility_base:
						etree.SubElement(asset, 'CompatibilityBase', VALUE=asset_data.compatibility_base)

					if asset_data.user_words and len(asset_data.user_words):
						userwords = etree.SubElement(asset, 'Userwords')
						for userword in asset_data.user_words:
							etree.SubElement(userwords, 'Userword', VALUE=userword)

					if asset_data.user_notes:
						etree.SubElement(asset, 'UserNotes').text=etree.CDATA(asset_data.user_notes or '')

			else:
				etree.SubElement(support_assets, 'SupportAsset', VALUE=('/' / relative_file_path).as_posix())

		if self.objects:
			objectcompatibilities = etree.SubElement(product, 'ObjectCompatibilities')
			for object in self.objects:
				etree.SubElement(objectcompatibilities, 'ObjectCompatibility', VALUE=object.uri, REF=object.scene_id)

		etree.indent(metadata, space=' ')
		return etree.tostring(metadata, encoding='UTF-8', xml_declaration=True, pretty_print=True)

	@property
	def metadata_script(self) -> str:
		return '''// DAZ Studio version 0.0.0.0 filetype DAZ Script

if( App.version >= 67109158 ) //4.0.0.294
{
	var oFile = new DzFile( getScriptFileName() );
	var oAssetMgr = App.getAssetMgr();
	if( oAssetMgr )
	{
		oAssetMgr.queueDBMetaFile( oFile.baseName() );
	}
}
'''

	@property
	def guess_tags(self) -> set[str]:
		tags: set[str] = set()

		if any(x for _, x in self._files() if x.suffix.lower() in _USER_FACING_DAZ_EXTENSIONS + _OTHER_DAZ_EXTENSIONS and not x.parent.as_posix().lower() == 'runtime/support'):
			tags.add('DAZStudio4_5')

		if any(x for _, x in self._files() if x.suffix.lower() in _USER_FACING_POSER_EXTENSIONS + _OTHER_POSER_EXTENSIONS and x.as_posix().lower().startswith('runtime/')):
			tags.add('DAZStudio4_5')
			tags.add('PoserLegacy')

		return tags or set(('General',))

	def __post_init__(self):
		self._merge_package_data(load_metadata(self.content_location))

		if self.url:
			self._merge_package_data(scrape(self.url))

		if not self.global_id:
			self.global_id = uuid4()

		if not self.prefix:
			self.prefix = 'LOCAL'

		if not self.store:
			self.store = 'LOCAL USER'

		if not self.tags:
			self.tags = self.guess_tags

	def _merge_package_data(self, package_data: PackageData) -> None:
		for field in fields(PackageData):
			if (not getattr(self, field.name)):
				setattr(self, field.name, getattr(package_data, field.name))

	def _assert_required_vars(self) -> None:
		requiredString: list[str] = []
		exceptions: list[Exception] = []

		if not self.prefix:
			requiredString.append('Source Prefix')

		if not self.sku:
			requiredString.append('Product SKU')

		if not self.name:
			requiredString.append('Product Name')

		if requiredString:
			exceptions.append(RuntimeError(f'Missing {', '.join(requiredString)}'))

		if not self.sanitized_name:
			exceptions.append(RuntimeError(f"Unable to generate sanitized product name from '{self.name}'"))

		if exceptions:
			raise ExceptionGroup('Required variables missing', exceptions)

	def _files(self):
		for root, _, files in self.content_location.walk():
			if not (rel_root := root.relative_to(self.content_location)).as_posix() == _SUPPORT_DIR:
				for file in files:
					path = Path(file)
					if '__MACOSX' not in path.parts and path.name.lower() not in _EXCLUDE_FILES and path.suffix.lower() not in _EXCLUDE_SUFFIXES:
						file_path = root / file
						if not (path.suffix.lower() == '.rsr' and file_path.with_suffix('.png').exists()):
							yield(file_path, rel_root / file)

	def _create_zip(self) -> None:
		_MANIFEST_FILE = 'Manifest.dsx'
		_SUPPLEMENT_FILE = 'Supplement.dsx'
		_README_FILE = 'ReadMe.pdf'

		if self.verbose:
			print('Generating ZIP file')

		self._assert_required_vars()

		# Use Windows-1252 encoding for filenames
		zipfile.ZipInfo = Windows1252_ZipInfo

		with zipfile.ZipFile(self.zip_filename, 'x', zipfile.ZIP_DEFLATED) as zip_file:
			# DIM Package
			zip_file.writestr(_MANIFEST_FILE, self.manifest_file)
			zip_file.writestr(_SUPPLEMENT_FILE, self.supplement_file)

			# ReadMe
			if isinstance(self.readme, Path):
				zip_file.write(self.readme, _README_FILE)
			elif isinstance(self.readme, bytes):
				zip_file.writestr(_README_FILE, self.readme)

			# Metadata
			zip_file.writestr(f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}.dsx', self.metadata_file)
			zip_file.writestr(f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}.dsa', self.metadata_script)
			if (image_extension := self.metadata_image_extension):
				if isinstance(self.image, Path):
					zip_file.write(self.image, f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}{image_extension}')
				elif isinstance(self.image, HTTPResponse) and self.image:
					zip_file.writestr(f'{_CONTENT_DIR}/{_SUPPORT_DIR}/{self.metadata_filename_base}{image_extension}', self.image.read())

			# Content
			if self.verbose:
				print('Adding Content')

			for file_path, relative_file_path, in self._files():
				# Compress DAZ compressable files before adding to archive
				if file_path.suffix.lower() in _COMPRESSABLE_DAZ_EXTENSIONS and file_path.stat().st_size:
					with gzip.open(file_path) as f:
						try:
							f.read(1)
							zip_file.write(file_path, _CONTENT_DIR / relative_file_path)
						except gzip.BadGzipFile:
							if self.verbose:
								print (f'Compressing: {relative_file_path}')
							with open(file_path, 'rb') as f:
								zip_file.writestr(zipfile.ZipInfo.from_file(file_path, (_CONTENT_DIR / relative_file_path).as_posix()), gzip.compress(f.read()))
				else:
					zip_file.write(file_path, _CONTENT_DIR / relative_file_path)

		# Revert filename encoding
		zipfile.ZipInfo = Ascii_ZipInfo

	def make_package(self) -> None:
		try:
			self._create_zip()
		except (FileExistsError) as e:
			sys.exit(e)	# pyright: ignore[reportArgumentType]