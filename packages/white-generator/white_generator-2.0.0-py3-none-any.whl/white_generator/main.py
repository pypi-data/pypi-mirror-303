import sys

import termcolor

from . import logger
from . import cli
from . import io
from . import db
from . import generation

def main() -> None:
    logger.init_logger()

    try:
        options = cli.parse_options()
        assert options.input_file is not None

        if not options.output_path.exists():
            options.output_path.mkdir(parents=True)

        db_connection = db.connect_to_db()
        for note in io.read_notes(options.input_file):
            note_id = io.generate_note_id(note)
            logger.get_logger().info(
                'generate an image for the %s note',
                termcolor.colored(note_id, 'blue'),
            )

            if not options.no_database:
                if not db.exists_in_db(db_connection, note):
                    db.insert_in_db(db_connection, note)
                else:
                    logger.get_logger().warning(
                        'note %s is duplicated',
                        termcolor.colored(note_id, 'blue'),
                    )
                    continue

            image = generation.generate_image(
                note,
                options.image,
                options.text,
                options.watermark,
            )
            image.save(options.output_path / (note_id + '.png'), 'PNG')
    except Exception as exception:
        logger.get_logger().error(exception)
        sys.exit(1)
    except KeyboardInterrupt:
        print('') # output a line break after the ^C symbol in a terminal
        sys.exit(1)
