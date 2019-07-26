def users(conn):
    print("List Users:")

    for user in conn.identity.users():
        print(user)


def credentials(conn):
    print("List Credentials:")

    for credential in conn.identity.credentials():
        print(credential)


def projects(conn):
    print("List Projects:")

    for project in conn.identity.projects():
        print(project)


def domains(conn):
    print("List Domains:")

    for domain in conn.identity.domains():
        print(domain)


def groups(conn):
    print("List Groups:")

    for group in conn.identity.groups():
        print(group)


def services(conn):
    print("List Services:")

    for service in conn.identity.services():
        print(service)


def endpoints(conn):
    print("List Endpoints:")

    for endpoint in conn.identity.endpoints():
        print(endpoint)


def regions(conn):
    print("List Regions:")

    for region in conn.identity.regions():
        print(region)


def roles(conn):
    print("List Roles:")

    for role in conn.identity.roles():
        print(role)


def role_domain_group_assignments(conn):
    print("List Roles assignments for a group on domain:")

    for role in conn.identity.role_domain_group_assignments():
        print(role)


def role_domain_user_assignments(conn):
    print("List Roles assignments for a user on domain:")

    for role in conn.identity.role_project_user_assignments():
        print(role)


def role_project_group_assignments(conn):
    print("List Roles assignments for a group on project:")

    for role in conn.identity.role_project_group_assignments():
        print(role)


def role_project_user_assignments(conn):
    print("List Roles assignments for a user on project:")

    for role in conn.identity.role_project_user_assignments():
        print(role)
