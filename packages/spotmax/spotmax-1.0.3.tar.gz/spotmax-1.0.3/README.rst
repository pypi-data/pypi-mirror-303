.. _GNU General Public License v3.0: https://github.com/ElpadoCan/spotMAX/blob/main/LICENSE
.. _Contributing Guide: https://spotmax.readthedocs.io/en/latest/misc/contributing.html
.. _installation guide: https://spotmax.readthedocs.io/en/latest/install/index.html
.. _PyPI: https://pypi.org/project/spotmax/
.. _Documentation: https://spotmax.readthedocs.io/en/latest
.. _Examples (notebooks, parameters files, etc.): https://github.com/SchmollerLab/SpotMAX/tree/main/examples
.. _Francesco Padovani: https://www.linkedin.com/in/francesco-padovani/
.. _Cell-ACDC: https://github.com/SchmollerLab/Cell_ACDC


.. |spotmaxlogo| image:: spotmax/docs/source/_static/logo.png
   :width: 64
   :target: https://github.com/ElpadoCan/spotMAX/tree/main/spotmax/resources

|spotmaxlogo| Welcome to SpotMAX!
=================================

*Written by* `Francesco Padovani`_ *(creator of* `Cell-ACDC`_ *) with feedback 
from* **tons of people**,  *see list of authors here* `Citation`_. 

A generalist framework for multi-dimensional automatic spot detection and quantification
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to **analyse fluorescence microscopy data** you are probably in the 
right place.

SpotMAX will help you with these **two tasks**:

1. Detect and quantify **globular-like structures** (a.k.a. "spots")
2. Segment and quantify **fluorescently labelled structures**

SpotMAX excels in particularly challenging situations, such as 
**low signal-to-noise ratio** and **high spot density**.

It supports **2D, 3D, 4D, and 5D data**, i.e., z-stacks, timelapse, and multiple 
fluorescence channels (and combinations thereof).

Installation
------------

SpotMAX is published on `PyPI`_, therefore it can simply be installed with::

    pip install spotmax

Depending on how you plan to use it, you will need additional packages. 
See here for the `installation guide`_

Resources
---------

- `Documentation`_
- `Examples (notebooks, parameters files, etc.)`_
- Pre-print
- X/Twitter thread
- Publication (working on it 🚀)

.. _Citation:

Citation
--------

If you use spotMAX in your work, please cire the following publication:

   Padovani, F., Čavka, I., Neves, A. R. R., López, C. P., Al-Refaie, N., 
   Bolcato, L., Chatzitheodoridou, D., Chadha, Y., Su, X.A., Lengefeld, J., 
   Cabianca D. S., Köhler, S., Schmoller, K. M. *SpotMAX: a generalist 
   framework for multi-dimensional automatic spot detection and quantification*,
   bioRxiv (2024) doi:

Contact
-------

**Do not hesitate to contact us** here on GitHub (by opening an issue)
or directly at the email elpado6872@gmail.com for any problem and/or feedback
on how to improve the user experience!

Contributing
------------

At SpotMAX we encourage contributions to the code! Please read our 
`Contributing Guide`_ 
to get started.

License
-------

SpotMAX is licensed under the `GNU General Public License v3.0`_
