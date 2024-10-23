import os
import shutil
import tarfile
import json
from gwml.cmdLib.getLagacyFile import decompress_file_to_file
from pkg_resources import resource_filename


class ModelOrganizer:
    def __init__(self, base_directory, whlTf):
        self.base_directory = base_directory
        self.bin_directory = os.path.join(base_directory, "bin")
        self.model_directory = os.path.join(base_directory, "model")
        self.env_directory = os.path.join(base_directory, "env")
        self.whlTf = whlTf
        # self.resource_path = pkg_resources.files("gwml.lagacy")

    def create_directories(self):
        os.makedirs(self.bin_directory, exist_ok=True)
        os.makedirs(self.model_directory, exist_ok=True)
        os.makedirs(self.env_directory, exist_ok=True)

    def copy_files(self, fileName):
        files_to_copy = {
            "bin": ["predict.py"],
            "model": ["model.py"],
            "env": ["requirements.txt"],
        }
        missing_files = []
        
        # Decompress the contents of the compressed file and save to the decompressed file
        # decompress_file_to_file(
        #     resource_filename("gwml", "/lagacy/train/{}".format(fileName)),
        #     os.path.join(self.bin_directory, "train.py"),
        # )

        for directory, files in files_to_copy.items():
            for file in files:
                src = os.path.join(self.base_directory, file)
                dst = os.path.join(self.base_directory, directory, file)
                if os.path.exists(src):
                    shutil.copy(src, dst)
                else:
                    missing_files.append(file)
        
        for file in os.listdir(self.base_directory):
            if ".py" in file and file not in ["train.py", "model.py", "predict.py"]:
                src = os.path.join(self.base_directory, file)
                dst = os.path.join(self.base_directory, "model", file)
                if os.path.exists(src):
                    shutil.copy(src, dst)

            # elif "train.py" == file:
            #     dst = os.path.join(self.base_directory, "bin", file)
            #     if os.path.exists(src):
            #         shutil.copy(src, dst)

        # Decompress the contents of the compressed file and save to the decompressed file
        decompress_file_to_file(
            resource_filename("gwml", "/lagacy/train/{}".format(fileName)),
            os.path.join(self.bin_directory, "train.py"),
        )

        if missing_files:
            raise FileNotFoundError(
                f"The following files are missing: {', '.join(missing_files)}"
            )

    def create_tar_gz(self, output_filename):
        output_filename = os.path.join(self.base_directory, output_filename)
        with tarfile.open(output_filename, "w:gz") as tar:
            tar.add(self.bin_directory, arcname="bin")
            tar.add(self.model_directory, arcname="model")
            tar.add(self.env_directory, arcname="env")
            tar.add("modelInfo.json")
            tar.add("hyperParamScheme.json")
            
            if self.whlTf:
                tar.add("download_packages")
                tar.add("run.sh")

    def save_json_to_file(self, json_data, file_path):
        with open(file_path, "w") as file:
            json.dump(json_data, file, indent=4)

    def clean_up(self):
        if os.path.exists(self.bin_directory):
            shutil.rmtree(self.bin_directory)
        if os.path.exists(self.model_directory):
            shutil.rmtree(self.model_directory)
        if os.path.exists(self.env_directory):
            shutil.rmtree(self.env_directory)
        # if os.path.exists("dockerfile"):
        #     os.remove("dockerfile")
        if os.path.exists("modelinfo.json"):
            os.remove("modelinfo.json")
        if os.path.exists("hyperParamScheme.json"):
            os.remove("hyperParamScheme.json")
        if os.path.exists("run.sh"):
            os.remove("run.sh")
        # if os.path.exists("download_packages"):
        #     shutil.rmtree("download_packages")
        

    def organize_and_compress(self, output_filename, fileName, modelInfo, hpoOpt):
        try:
            self.create_directories()
            self.save_json_to_file(modelInfo, "./modelInfo.json")
            self.save_json_to_file(hpoOpt, "./hyperParamScheme.json")
            self.copy_files(fileName)
            self.create_tar_gz(output_filename)
            print(f"Files successfully organized and compressed into {output_filename}")
        except FileNotFoundError as e:
            print(e)
        finally:
            print("done")
            self.clean_up()


# # Usage
# base_directory = '.'  # 현재 디렉토리
# output_filename = 'X.tar.gz'

# organizer = FileOrganizer(base_directory)
# organizer.organize_and_compress(output_filename)
