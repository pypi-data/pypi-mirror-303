# PYTHON LIBRARIES
# ========================================
from fastapi import FastAPI
from fastapi.routing import APIRoute
from pydantic import BaseModel
from collections import defaultdict

# MODULE LIBRARIES
# ========================================


# ========================================
# CLASS
# ========================================


class FastApiValidityCheck(BaseModel):
    is_valid: bool = True
    message: str = "Apps are valid"


# ========================================
# FUNCTIONS
# ========================================


def check_fast_api_validity(*args: FastAPI) -> FastApiValidityCheck:
    """
    Checks the validity of the provided fast api apps :
    - no apps have the same title
    - no app have the same routes and method
    - no apps have the same route functions


    Returns:
        FastApiValidityCheck: A summary of the validity of the provided fast api apps
    """

    # APPS HAVE THE SAME TITLE
    same_title_check = _check_app_titles(*args)
    if not same_title_check.is_valid:
        return same_title_check

    # APPS HAVE THE SAME ROUTES
    same_routes_check = _check_app_routes(*args)
    if not same_routes_check.is_valid:
        return same_routes_check

    # APPS HAVE THE SAME FUNCTIONS
    same_functions_check = _check_app_functions(*args)
    if not same_functions_check.is_valid:
        return same_functions_check

    return FastApiValidityCheck()


# ========================================
# PRIVATE FUNCTIONS
# ========================================
def _check_app_titles(*args: FastAPI) -> FastApiValidityCheck:
    """
    Checks that none of the provided apps have the same title

    Args:
        apps (tuple[FastAPI]): The FastAPI apps to check.

    Returns:
        FastApiValidityCheck: a FastApiValidityCheck object with the validation result.

    """

    app_titles: list[str] = [app.title for app in args]

    duplicates = _find_duplicates_with_counts(app_titles)

    if len(duplicates) > 0:
        is_valid = False
        message = f"Apps have the same title : {duplicates}"
        return FastApiValidityCheck(is_valid=is_valid, message=message)
    else:
        return FastApiValidityCheck()


def _find_duplicates_with_counts(input_list: list[str]) -> dict[str, int]:
    """
    Returns the duplicates and their number of occurrences in the input list.

    Args:
        input_list (list[str]): _description_

    Returns:
        dict[str, int]: _description_
    """
    element_count = {}
    duplicates = {}

    # Count occurrences of each element
    for item in input_list:
        element_count[item] = element_count.get(item, 0) + 1

    # Find elements that appear more than once and store their counts
    for item, count in element_count.items():
        if count > 1:
            duplicates[item] = count

    return duplicates


def _check_app_routes(*apps: FastAPI) -> FastApiValidityCheck:
    """
    Checks that none of the provided apps have the same routes and method

    Args:
        apps (tuple[FastAPI]): The FastAPI apps to check.

    Returns:
        FastApiValidityCheck: a FastApiValidityCheck object with the validation result.
    """

    route_registry = defaultdict(list)
    conflicts = []

    # Iterate through all apps and register their routes
    for app in apps:

        routes = [route for route in app.routes if isinstance(route, APIRoute)]
        for route in routes:

            # Collect route path and method (GET, POST, etc.)
            path = route.path
            methods = route.methods

            for method in methods:
                # If the route and method already exist, it means a conflict
                if (path, method) in route_registry:
                    conflicts.append((path, method))
                route_registry[(path, method)].append(app)

    # If conflicts exist, return invalid status
    if len(conflicts):

        message = f"Apps have the same routes and method : {conflicts}"
        return FastApiValidityCheck(is_valid=False, message=message)

    return FastApiValidityCheck()


def _check_app_functions(*apps: FastAPI) -> FastApiValidityCheck:
    """
    Checks that none of the provided apps have the same route functions (endpoints).

    Args:
        apps (tuple[FastAPI]): The FastAPI apps to check.

    Returns:
        FastApiValidityCheck: a FastApiValidityCheck object with the validation result.
    """
    function_registry = defaultdict(list)
    conflicts = []

    # Iterate through all apps and register their route functions
    for app in apps:
        routes = [route for route in app.routes if isinstance(route, APIRoute)]
        for route in routes:
            # Collect route function (endpoint)
            route_function = route.name

            # If the function already exists in the registry, we mark it as a conflict
            if route_function in function_registry:
                conflicts.append((route.path, route_function))
            function_registry[route_function].append(app)

    # If conflicts exist, return invalid status
    if conflicts:
        messsage = f"Apps have the same route functions : {conflicts}"
        return FastApiValidityCheck(is_valid=False, message=messsage)

    return FastApiValidityCheck(is_valid=True)
