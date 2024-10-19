# This module contains the implementation for listing external references.


from . import content
from . import error
from . import id
from . import misc


# Category titles, keyed by label.
titles = {}


################################################################################
# Public API
#
# Items in this area are documented and exported for use by end users.
################################################################################


@error.exit_on_script_error
@misc.setup_only
def add_reference_category(title, label):
    """Creates a topic for listing external references.

    This function does not create any actual references; they must be
    added to each test individually with the ``references`` argument of
    :py:class:`atform.Test`. This function is only available in the setup
    area of the script before any tests or sections are created.

    .. seealso:: :ref:`ref`

    Args:
        title (str): The full name of the category that will be displayed
            on the test documents.
        label (str): A shorthand abbreviation to identify this category
            when adding references to individual tests. Must be unique across
            all reference categories.
    """
    global titles

    # Validate title.
    title_stripped = misc.nonempty_string("reference category title", title)

    # Validate label.
    label_stripped = misc.nonempty_string("reference category label", label)
    if label_stripped in titles:
        raise error.UserScriptError(
            f"Duplicate reference label: {label_stripped}",
            f"Create a unique label for {title} references.",
        )

    titles[label_stripped] = title_stripped


def get_xref():
    """Builds a cross-reference of tests assigned to each reference.

    For use in the output section of a script, after all tests have
    been defined.

    .. seealso:: :ref:`xref`

    Returns:
        dict: A cross-reference between tests and references represented as a
        nested dictionary. The top-level dictionary is keyed by category labels
        defined with :py:func:`atform.add_reference_category`; second-level
        dictionaries are keyed by references in that category, i.e., items
        passed to the ``references`` argument of :py:class:`atform.Test`.
        Final values of the inner dictionary are lists of test identifiers,
        formatted as strings, assigned to that reference. As an example,
        the keys yielding a list of all tests assigned ``"SF42"`` in the
        ``"sf"`` category would be ``["sf"]["SF42"]``.
    """
    global titles

    # Initialize all categories with empty dictionaries, i.e., no references.
    xref = {label: {} for label in titles}

    # Iterate through all Test instances to populate second-level
    # reference dictionaries and test lists.
    for test in content.tests:
        test_id = id.to_string(test.id)
        for cat in test.references:
            for ref in test.references[cat]:
                xref[cat].setdefault(ref, []).append(test_id)

    return xref
