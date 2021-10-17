# Share Documents
An open-source platform where companies can share documents with clients, shareholders or anyone under their own branding.

## Installation

Clone the project using ```git``` and ```cd``` into the folder.

```bash
git clone https://github.com/Idiomatic-Programmers/ShareDocument.git
cd ShareDocument
```
Install all the dependencies using ```pip```
```bash
pip install -r requirements.txt
```

## Usage
Migrate the database

```bash
python manage.py migrate
```
Create a superuser
```bash
python manage.py createsuperuser
```
Run the server
```bash
python manage.py runserver
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

For more information, please refer the CONTRIBUTION.md file

## License
[MIT](https://choosealicense.com/licenses/mit/)
