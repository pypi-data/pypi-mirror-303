# Development

## Tests

Tests are run using PyTest. You can simply run this command to launch tests:

```bash
pytest
```

## Documentation

High-level documentation is handled by [Typer](https://typer.tiangolo.com/). You can update the generated `USAGE.md` file using this command:

```bash
make docs
```

[Mkdocs](https://www.mkdocs.org/) is also used to generate a clean web page for documentation, you can check out its rendering by launching:

```bash
pip install -e .[docs]
mkdocs serve
```

## Translations

Translations and internationalization are managed with Python `gettext`. Translations files are located in `geopic_tag_reader/geopic_tag_reader/translations/` folder. You can make a string in code translated using:

```python
# Load i18n module
from geopic_tag_reader.i18n import init as i18n_init

# Create translator with appropriate language
_ = i18n_init("fr")

# Use _ function to translate
print(_("My label is {mood}").format(mood="good"))
```

Once you have done all your translations, run this command to update the POT label catalog (you will need to have the [`gettext` utilities](https://www.gnu.org/software/gettext/) installed):

```bash
make i18n-code2pot
```

Then, our translations are managed through [our Weblate instance](https://weblate.panoramax.xyz/).

If you want to convert translated PO files into MO files, you can run:

```bash
make i18n-po2code
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Note that before opening a pull requests, you may want to check formatting and tests of your changes:

```bash
make ci
```

You can also install git [pre-commit](https://pre-commit.com/) hooks to format code on commit with:

```bash
pip install -e .[dev]
pre-commit install
```

## Make a release

```bash
git checkout develop
git pull

vim CHANGELOG.md					# Edit version + links at bottom
vim geopic_tag_reader/__init__.py	# Edit version
make prepare_release

git add *
git commit -m "Release x.x.x"
git tag -a x.x.x -m "Release x.x.x"
git push origin develop
git checkout main
git merge develop
git push origin main --tags
```
