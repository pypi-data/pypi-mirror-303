@REM I tried setting pip.ini settings but it didn't wok

@REM [distutils]
@REM index-servers =
@REM     pypi
@REM     testpypi

@REM [pypi]
@REM username = __token__
@REM password = pypi-AgEIcHlwaS5vcmcCJDI3MmZkNDQxLTU0ZDctNDJkZC1hNWNjLWExNjE3OTBlNGQ1YgACKlszLCJkODBiNjg2ZS05ODFiLTRhMTAtOGQ2ZS04MmU2ODZmNjQ3NDMiXQAABiCsZc8alT2fCsi7pGbVt9z_C2CeXCI7YhuKAz9ntgbYYA

@REM Instead, I set the TWINE_USERNAME and TWINE_PASSWORD as environment variable and that did work.
@REM However, the testpypi needs a token of its own.

python -m build
twine check dist/*
twine upload -r testpypi dist/*
twine upload -r pypi dist/*