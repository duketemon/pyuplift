######################
Contribute to pyuplift
######################
Everyone is more than welcome to contribute. It is a way to make the project better and more accessible to more users.

**Guidelines**

* `Submit Pull Request`_
* `Git Workflow Howtos`_

  - `How to resolve conflict with master`_
  - `How to combine multiple commits into one`_
  - `What is the consequence of force push`_

* `Documents`_

*******************
Submit Pull Request
*******************

* Before submit, please rebase your code on the most recent version of master, you can do it by

  .. code-block:: bash

    git remote add upstream https://github.com/duketemon/pyuplift
    git fetch upstream
    git rebase upstream/master

* If you have multiple small commits,
  it might be good to merge them together(use git rebase then squash) into more meaningful groups.
* Send the pull request!

  - Fix the problems reported by automatic checks
  - If you are contributing a new module, consider add a testcase

*******************
Git Workflow Howtos
*******************

How to resolve conflict with master
===================================
- First rebase to most recent master

  .. code-block:: bash

    # The first two steps can be skipped after you do it once.
    git remote add upstream https://github.com/duketemon/pyuplift
    git fetch upstream
    git rebase upstream/master

- The git may show some conflicts it cannot merge, say ``conflicted.py``.

  - Manually modify the file to resolve the conflict.
  - After you resolved the conflict, mark it as resolved by

    .. code-block:: bash

      git add conflicted.py

- Then you can continue rebase by

  .. code-block:: bash

    git rebase --continue

- Finally push to your fork, you may need to force push here.

  .. code-block:: bash

    git push --force

How to combine multiple commits into one
========================================
Sometimes we want to combine multiple commits, especially when later commits are only fixes to previous ones,
to create a PR with set of meaningful commits. You can do it by following steps.

- Before doing so, configure the default editor of git if you haven't done so before.

  .. code-block:: bash

    git config core.editor the-editor-you-like

- Assume we want to merge last 3 commits, type the following commands

  .. code-block:: bash

    git rebase -i HEAD~3

- It will pop up an text editor. Set the first commit as ``pick``, and change later ones to ``squash``.
- After you saved the file, it will pop up another text editor to ask you modify the combined commit message.
- Push the changes to your fork, you need to force push.

  .. code-block:: bash

    git push --force

What is the consequence of force push
=====================================
The previous two tips requires force push, this is because we altered the path of the commits.
It is fine to force push to your own fork, as long as the commits changed are only yours.

*********
Documents
*********
* Documentation is built using sphinx.
* Each document is written in `reStructuredText <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.
* You can build document locally to see the effect.

