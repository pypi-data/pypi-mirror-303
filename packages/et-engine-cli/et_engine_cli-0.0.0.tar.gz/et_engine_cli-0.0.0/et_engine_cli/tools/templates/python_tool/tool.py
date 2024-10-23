import os
import logging
import sys

from et_engine.tools import ArgParser, Logger

from <<{{TOOL_NAME}}>> import main


if __name__ == "__main__":

    args = ArgParser(name="<<{{TOOL_NAME}}>>")
    
    args.add_argument('log_file', required=False, type=str, default="", description='relative path to the log file')

    if args.log_file:
        log_file = os.path.join("/filesystems", args.filesystem_name, args.log_file)
        logger = Logger(log_file, append=True)
    else:
        logger = logging.getLogger(__name__)
        logging.basicConfig(stream=sys.stdout, level=logging.INFO, format='%(message)s')

    logger.info(str(args))

    main(args, logger)