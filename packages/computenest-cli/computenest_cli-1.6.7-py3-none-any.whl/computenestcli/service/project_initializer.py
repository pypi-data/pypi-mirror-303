import subprocess
import os
import click
import tarfile
import traceback

BUCKET_NAME = 'computenest-service-templates'


class ProjectInitializer:
    def __init__(self, project_name, output_path):
        self.project_name = project_name
        self.output_path = output_path

    def download_project(self):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        tarball_url = f'https://{BUCKET_NAME}.oss-cn-hangzhou.aliyuncs.com/{self.project_name}.tar.gz'
        tarball_path = os.path.join(self.output_path, f'{self.project_name}.tar.gz')

        try:
            click.echo(f'Downloading {tarball_url} to {tarball_path}')
            subprocess.check_call(['wget', '-q', tarball_url, '-O', tarball_path])
            click.echo(f'Successfully downloaded {self.project_name}.tar.gz to {tarball_path}')
            self.extract_tarball(tarball_path, self.output_path)
        except subprocess.CalledProcessError as e:
            click.echo(f'Error downloading {self.project_name}.tar.gz: {e}')
            traceback.print_exc()
        except Exception as e:
            click.echo(f'Unexpected error: {e}')
            traceback.print_exc()

    def extract_tarball(self, tarball_path, extract_to):
        # 解压 .tar.gz 文件到指定目录
        try:
            with tarfile.open(tarball_path, "r:gz") as tar:
                tar.extractall(path=extract_to)
            click.echo(f'Successfully extracted {tarball_path} to {extract_to}')
            os.remove(tarball_path)  # 删除下载的 .tar.gz 文件
        except tarfile.TarError as e:
            click.echo(f'Error extracting {tarball_path}: {e}')
            traceback.print_exc()
        except Exception as e:
            click.echo(f'Unexpected error: {e}')
            traceback.print_exc()
