Filesystems Commands
====================

.. automodule:: et_engine_cli.filesystems.commands
   :members:
   :undoc-members:
   :show-inheritance:

.. click:: et_engine_cli.filesystems.commands:fs
   :prog: et fs
   :nested: full

Helper Functions
----------------

.. autofunction:: et_engine_cli.filesystems.commands.check_api_key
   :noindex:

Constants
---------

.. autodata:: et_engine_cli.filesystems.commands.MIN_CHUNK_SIZE_BYTES
   :annotation: Minimum chunk size for multipart operations

Error Handling
--------------

This module uses exception handling to manage errors, including:

- :class:`et_engine.errors.AuthenticationError`: Handled specifically in the `list` command.
- :class:`FileNotFoundError`: Handled specifically in the `mkdir` command.
- General :class:`Exception` handling for all commands to catch any unexpected errors.

For detailed error messages, refer to the individual command outputs.