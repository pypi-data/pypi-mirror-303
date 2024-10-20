import setuptools

setuptools.setup(
    # Includes all other files that are within your project folder
    include_package_data=True,
    # Name of your Package
    name="fast2app",
    # Project Version
    version="1.1",
    # python version
    python_requires=">=3.11",
    # docfiles
    doc_files="README.md",
    # Description of your Package
    description="""A simple tool designed to automatically generate usable types, functions, and
    other useful server-side code from a list of [FastAPI](https://fastapi.tiangolo.com/) application to
    a given framework.""",
    # Website for your Project or Github repo
    url="https://git.mydh.io/shared/fast2app",
    project_urls={
        "Nuxt Documentation": "https://git.mydh.io/shared/fast2app/-/blob/development/NUXT_DOCUMENTATION.md",
        "Help Desk": "https://helpdesk.mydh.io/issue-form",
        "Contact and contribution": "https://helpdesk.mydh.io/contact-form",
        "Bug Tracker": "https://git.mydh.io/shared/fast2app/-/issues/?sort=priority&state=opened&label_name%5B%5D=bug&first_page_size=20",
    },
    keywords=[
        "fastapi",
        "nuxt",
        "composable",
        "api",
        "generation",
        "typescript",
        "framework",
        "backend",
        "frontend",
    ],
    # Projects you want to include in your Package
    packages=setuptools.find_namespace_packages(where="source"),
    package_dir={"": "source"},
    package_data={
        # NUXT
        "fast2app.export.nuxt.templates": ["*.ts"],
        "fast2app.export.nuxt": ["*.toml"],
    },
    # Dependencies/Other modules required for your package to work
    install_requires=[
        "pydantic",
        "fastapi",
        "pydantic-to-typescript2",
        "jinja2",
        "camel_converter",
        "regex",
        "astroid",
        "toml",
    ],
    entry_points={
        "console_scripts": ["fast2nuxt=fast2app.command_line.fast2nuxt:main"],
    },
)
