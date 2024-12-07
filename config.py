from dotenv import dotenv_values

# This is the letter template, where {santa} and {recipient} are automatically
# replaced by the secret santa's name, and his/her recipient of their gift
email_template = {
    "from_name": "Babbo Natale da Casært",
    "from_email": dotenv_values("./.env.secret")["SMTP_FROM"],
    "subject": "🎅🏻 Secret Santa 2024 🤫",
    "body": """
        Ho Ho Ho! 🎄✨

        Ciao {santa}, sei il Secret Santa di... {recipient}!

        Mi raccomando:
        ▸ pensa bene al regalo 🎁 
        ▸ mantieni il segreto! 🤐

        ✨ Buon divertimento e... buon Natale! 🎄🎅🏻
    """,
}

# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values)
# If there are no incompatibles, leave this dictionary empty.
incompatibles = {
    # # Do not allow James to be santa for Mary
    # 'James': ('Mary',),
    # # Do not allow Mary to be santa for James
    # 'Mary': ('James',),
    # # Do not allow Nancy to be santa for John or Mary
    # 'Nancy': ('John', 'Mary',),
    # # Something like below is bad, Linda can't be a secret santa for anyone!
    # 'Linda': ('James', 'Mary', 'Nancy', 'John', 'Michael', 'Lisa', 'David'),
}

# DON'T PEAK INTO THIS FILE!
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa
secret_santa_record_file = "secret-santa-record-file.txt"
