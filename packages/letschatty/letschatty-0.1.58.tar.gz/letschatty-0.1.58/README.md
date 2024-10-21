# Chatty Analytics
Models and custom classes to work across the Chattyverse

Chatty Analytics is a proprietary tool developed by Axel Gualda. This software is for internal use only and is not licensed for distribution or use outside of authorized contexts.

Copyright (c) 2024 Axel Gualda. All Rights Reserved.


poetry version patch
poetry build                                                
poetry publish -r testpypi
pip cache purge                                             
pip uninstall letschatty -y
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple letschatty
pytest -v tests/unit/models/messages/test_message_from_db.py

pip cache purge                                             
pip uninstall letschatty -y
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple letschatty
pytest -v tests/unit/models/messages/test_message_from_db.py