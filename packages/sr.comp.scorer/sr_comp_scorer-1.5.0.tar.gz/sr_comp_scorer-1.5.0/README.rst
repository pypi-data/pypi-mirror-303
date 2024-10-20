SRComp Scorer
=============

|Build Status|

A web UI to edit scores from SRComp score files.

Deployment
----------

For using the scorer at an event:

.. code:: shell

    script/install.sh

The install script prints instructions regarding the setup of the corresponding
compstate as well as how to run the resulting instance. Currently this is aimed
at install on a user's own machine rather than being hosted externally.

Development
-----------

**Install**:

.. code:: shell

    pip install -e .

**Run**:
``python -m sr.comp.scorer`` (see the ``--help``) for details.

Developers may wish to use the `SRComp Dev`_ repo to setup a dev instance.


.. |Build Status| image:: https://circleci.com/gh/PeterJCLaw/srcomp-scorer.png?branch=main
   :target: https://circleci.com/gh/PeterJCLaw/srcomp-scorer

.. _`SRComp Dev`: https://github.com/PeterJCLaw/srcomp-dev
