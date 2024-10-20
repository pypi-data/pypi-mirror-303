from pathlib import Path
from typing import Union


def generate_qrc(source_dir: Union[str, Path]) -> None:
    if isinstance(source_dir, str):
        source_dir = Path(source_dir)
    output_file = source_dir / 'resources.qrc'

    print('generating', output_file)

    with output_file.open('w') as f:
        f.write('<RCC>\n')
        f.write('  <qresource>\n')
        for item in source_dir.rglob('*'):
            if item.is_dir():
                continue
            elif item.suffix in ('.png', '.jpg', '.ico', '.qm', '.qss'):
                item = item.relative_to(source_dir).as_posix()
                print(item)
                f.write(f'    <file>{item}</file>\n')
        f.write('  </qresource>\n')
        f.write('</RCC>')


if __name__ == '__main__':
    generate_qrc(str(Path(__file__).parents[1] / 'assets'))
