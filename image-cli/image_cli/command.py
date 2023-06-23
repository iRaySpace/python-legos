import os
import click
from pdf2image import convert_from_path


@click.command('convert')
@click.argument('input_path')
def convert(input_path):
    click.echo(f'Converting {input_path}...')
    images = convert_from_path(input_path) # has a function that checks if the file exists

    filename, _ = input_path.split('.')
    result_path = f'res/{filename}'
    if not os.path.exists(result_path):
        os.makedirs(result_path)
        click.echo(f'Created {result_path} folder...')

    total_images = len(images)
    for i, page in enumerate(images):
        image_path = f'{result_path}/{i + 1}.jpg'
        page.save(image_path, 'JPEG')
        click.echo(f'Converted {i + 1}/{total_images}, saved at {image_path}.')
    click.echo(f'Finished converting {input_path}...')
