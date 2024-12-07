# Secret Santa 🎅🏻

This project will automatically "pull from a hat" a recipient for
every secret Santa and send a notification email to each Santa's inbox
of who their gift recipient is 🎁

It ensures that no one knows who their secret Santa is... **not even you** – unless you really want to know!

## Table of Contents

- [Configuration](#configuration)

- [Usage](#usage)

   - [Perform a dry run](#perform-a-dry-run)

   - [Test your SMTP configuration](#test-your-smtp-configuration)

   - [Send the emails](#send-the-emails)

## Configuration

Clone the repository and install dependencies via [poetry](https://python-poetry.org/docs/) with `poetry install`, then activate the virtual environment via the `poetry shell` command.

Make your desired modifications to the `config.py` configuration file (mostly the email template, optionally a lookup of anyone who should not be someone elses Santa).

Create a `.env.secret` file with a structure like that of `.env.shared` and specify:

-  the SMTP settings, as specified by your SMTP host;
-  the list of secret Santas (names and email addresses).

## Usage

### Perform a dry run

- `python ./secret-santa-mailer.py`

This will read the configuration file and perform a "dry run" of the various
pairings between secret Santas and recipients. It will generate an output file
as specified by the `secret_santa_record_file` setting in `config.py`.

This record file is saved as `secret-santa-record-file.txt` by default.

### Test your SMTP configuration

Send a test email to confirm that the SMTP configuration is set up correctly:

- `python ./secret-santa-mailer.py --send-test-email you@example.com`

If it runs without any error, then you're ready to send the secret Santa
emails.

### Send the emails

- `python ./secret-santa-mailer.py --official`

This will sequentially send emails to everyone and record them into the file specified
by the `secret_santa_record_file` setting in `config.py`.

⚠️ *Don't look at the contents of this file, unless you want to know who everyone's
secret Santa is!*

Enjoy, and have a Merry Christmas! 🎄