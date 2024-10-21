import re

from .fragments import fragments


def extract_fragment_names(query_or_fragment: str) -> set[str]:
    """Extracts fragment names from a given GraphQL query or fragment.

    :param query_or_fragment: The GraphQL query or fragment string.
    :type query_or_fragment: str
    :return: A set of fragment names used in the query or fragment.
    :rtype: set[str]
    """
    pattern = re.compile(r'\.\.\.(\w+)')  # extracts WORD from  ...WORD
    return set(pattern.findall(query_or_fragment))


def resolve_fragments(
    fragments_to_resolve: set[str], resolved_fragments: set[str] | None = None
) -> set[str]:
    """Recursively resolve all nested fragments required for a given fragment.

    :param fragments_to_resolve: The set of fragment names that need to be resolved.
    :param resolved_fragments: A set of resolved fragment names (used in recursion).
    :return: A set of all required fragment names.
    :raises ValueError: If a fragment name is not found in the fragments dictionary.
    """
    if resolved_fragments is None:
        resolved_fragments = set()

    for fragment_name in fragments_to_resolve:
        if fragment_name in resolved_fragments:
            continue

        fragment_body = fragments[fragment_name]
        if not fragment_body:
            raise ValueError(f"Fragment '{fragment_name}' not found.")

        resolved_fragments.add(fragment_name)
        nested_fragments = extract_fragment_names(fragment_body)
        resolve_fragments(nested_fragments, resolved_fragments)

    return resolved_fragments


def clean_graphql_query(query: str) -> str:
    """Cleans a GraphQL `query` by removing comments, extra whitespaces, and spacing.

    :param query: The GraphQL query string.
    :type query: str
    :return: The cleaned GraphQL query string.
    :rtype: str
    """
    query = re.sub(r'#.*', '', query)
    query = re.sub(r'\s+', ' ', query)
    query = re.sub(r'\s*([{}()\[\],:])\s*', r'\1', query)
    return query.strip()


def build_full_query(query: str) -> str:
    """Builds the full GraphQL query by resolving and appending all necessary fragments.

    :param query: The base GraphQL query string.
    :type query: str
    :return: The full GraphQL query string with all required fragments.
    :rtype: str
    """
    fragments_used = extract_fragment_names(query)
    fragments_required = resolve_fragments(fragments_used)

    fragment_section = '\n'.join(
        [fragments[fragment_name] for fragment_name in fragments_required]
    )

    full_query = f'{fragment_section}\n{query}'
    return clean_graphql_query(full_query)
