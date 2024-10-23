import zlib
import zipfile
import pathlib

def package_version(package_name):
    package = __import__(package_name)

    try:
        package_version = package.__version__
    except:
        from importlib.metadata import version  
        package_version = version(package_name)

    return f"{package_name}: {package_version}" 

def compress_files(path=".", files=[], compression=zipfile.ZIP_DEFLATED, zip_filename="my.zip"):
    with zipfile.ZipFile(zip_filename, mode="w") as zf:
        try:
            for filename in files:
                file_to_zip = f"{path}/{filename}"
                zf.write(file_to_zip, compress_type=compression)
        except FileNotFoundError:
            print("FileNotFoundError:")
            print(file_to_zip)
        finally:
            zf.close()

def compress_folder(path=".", compression=zipfile.ZIP_DEFLATED, zip_filename="my.zip"):
    path = pathlib.Path(path)

    with zipfile.ZipFile(zip_filename, mode="w") as archive:
        for file_path in path.iterdir():
            archive.write(file_path, arcname=file_path.name, compress_type=compression)