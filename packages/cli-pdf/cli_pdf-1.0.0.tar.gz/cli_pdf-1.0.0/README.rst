cli-pdf
========

**cli-pdf** is a command-line tool that provides various functionalities for PDF manipulation, including encryption, decryption, splitting, merging, and renaming PDF fields.

Features
--------

- Encrypt and decrypt PDF files using a password.
- Split PDF files by specifying a page number.
- Merge two PDF files into one.
- Rename form fields in a PDF.
- Read and save field names from PDF forms.

Installation
------------

You can install **cli-pdf** via pip:

.. code-block:: bash

    pip install cli-pdf

Alternatively, you can install it from source by cloning the repository:

.. code-block:: bash

    git clone https://github.com/Personal-DevTools/cli-pdf
    cd cli-pdf
    pip install .

Usage
-----

Once installed, you can use the tool from the command line with the ``pdftool`` command:

.. code-block:: bash

    pdftool -i input.pdf -o output.pdf --encrypt -p "yourpassword"

Command-line options:

- ``-i``, ``--input``: Specify the input PDF file.
- ``-o``, ``--output``: Specify the output PDF file.
- ``-rf``, ``--readfieldnames``: Read and print form field names in the PDF.
- ``-rn``, ``--renamefieldnames``: Rename form field names using a JSON mapping.
- ``-m``, ``--merge``: Merge two PDF files.
- ``-s``, ``--split``: Split a PDF at a specific page number.
- ``-dc``, ``--decrypt``: Decrypt a PDF with a password.
- ``-ec``, ``--encrypt``: Encrypt a PDF with a password.
- ``-p``, ``--password``: Specify the password for encryption/decryption.

Examples
--------

- **Encrypting a PDF**:

  .. code-block:: bash

      pdftool -i input.pdf -o encrypted.pdf --encrypt -p "yourpassword"

- **Decrypting a PDF**:

  .. code-block:: bash

      pdftool -i encrypted.pdf -o decrypted.pdf --decrypt -p "yourpassword"

- **Splitting a PDF at page 3**:

  .. code-block:: bash

      pdftool -i input.pdf --split 3

- **Merging two PDFs**:

  .. code-block:: bash

      pdftool -i file1.pdf -m file2.pdf -o merged.pdf

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

Contributing
------------

Contributions are welcome! Please submit a pull request on the `GitHub repository <https://github.com/personal-devtools/cli-pdf>`_.
