.. _configuration_template:

Configuration template
======================

Global attributes
-----------------

This file can be used to configure the global attributes, there are two separate configuration steps:

    **Input:** Global attributes from a list of cubes are unified among the cubes.

    **Output:** Global attributes are created and added to a list of cubes.


The I/O configuration steps can be applied with the functions:

    :func:`gordias.config.configure_global_attributes_input`
    :func:`gordias.config.configure_global_attributes_output`

Input
~~~~~

The input configuration has three sections: default, drop, and transfer.

Default
^^^^^^^
The default configuration can be used to specify how to handle global attributes from the input files.
::

    default: <option>

The following two options are available:

    **equalize**: keep all attributes that are equal between the cubes

    **drop**: remove all attributes


Drop
^^^^
The drop configuration can be used to specify specific existing global attributes that should be removed.
::

    drop:
        - existing_attribute

E.g., this can be useful if the default option is `equalize` but you do not want to keep the global attribute
`institution` that is the same for all input cubes, then:
::

    drop:
        - institution

will remove the global attribute `institution` from all the cubes in the cube list.



Transfer
^^^^^^^^
The transfer configuration allows the user to specify specific global attributes to keep or join together with other global attributes.
::

    transfer:
        attr_name_1:
        - existing_attribute_1
        attr_name_2:
        - existing_attribute_2
        - existing_attribute_3

Here, `attr_name_x` determines the name for the
new global attribute, while `existing_attribute_x` determines which existing global attributes that should be transferred to `attr_name_x`, e.g., ::

    transfer:
        frequency:
        - frequency

creates the new global attribute `frequency` with the unique value from the input cubes: ::

    frequency = "day"

If `existing_attribute_x` has different values between cubes, the unique values will be joined with a comma separator, e.g., ::

    transfer:
        creation-dates:
        - creation_date

creates the new global attribute `creation-dates` with the joined values from the input cubes: ::

    creation-dates = "2018-06-21-T20:03:01Z, 2018-06-21-T19:59:31Z"

If the user defines multiple existing global attributes they will first be joined with an underscore and then the unique values will be
joined with a comma separator, e.g., ::

    transfer:
        tracking_and_creation:
        - tracking_id
        - creation_date

creates the new global attribute `tracking_and_creation` with the joined values from the input cubes::

    tracking_and_creation = "1a76c102-ed05-4d84-bfeb-e4dc1c48a5dc_2018-06-21-T20:03:01Z, df8c2f0a-4126-4c05-aafa-db532304cdcc_2018-06-21-T19:59:31Z"


Output
~~~~~~

The output configuration has one section: create.

Create
^^^^^^
The create configuration allows the user to specify their own global attributes.
::

    create:
        my_attr_name: "my global attribute value"

E.g., if the user wants to use their own institution ::

    create:
        institution: "SMHI"

it will create the global attribute: ::

    institution = "SMHI"


.. note:: If the choosen name of the global attribute has the same name as an already existing global attribute, either in the input configuration or in the cube's global attributes, it will overwrite the existing attribute.

It is also possible to fill in useful information that is fetched during the run time, e.g., existing global attributes, the software version, and time. Valid values are:

    {NOW}: creation date

    {TRACKING_ID}: tracking id (uuid)

    {CF_CONVENTIONS_VERSION}: CF-convention version supported by iris

    {existing_attribute}: existing global attributes in the cube

    {GORDIAS_VERSION}: gordias version

::

    create:
        creation_date: "{NOW}"
        tracking_id: "{TRACKING_ID}"
        software: "{GORDIAS_VERSION}"
        Conventions: "{CF_CONVENTIONS_VERSION}"
        rcm-gcm: "rcm: {rcm} gcm: {gcm}"


can create the output attributes::

    creation-date = "2023-03-31T14:52:32Z"
    tracking_id: "f299a24d-63ba-4f8d-a81d-0621be5b7ea5"
    software = "gordias-0.3.0"
    Conventions: "CF-1.7"
    rcm-gcm: "rcm: SMHI-RCA4_v1 gcm: NCC-NorESM1-M"


Default configuration-file
--------------------------

.. code-block:: yaml
    :caption: config.yml

    ---
    config:
    global_attributes:
        input:
            default: equalize
            drop:
                # CORDEX and CMIP attributes that are transferred (see below)
                - driving_experiment_name
                - model_id
                - rcm_version_id
                - driving_model_id
                - tracking_id
                - creation_date
                - driving_model_ensemble_member
                - history
                - history_of_appended_files
                - institution
                - institute_id
                - references
                - product
                - contact
                - software
                - project_id
                - experiment
                - experiment_id
                - driving_experiment
                - initialization_method
                - physics_version
                - realization
                - source
                - table_id
                - title
            transfer:
                scenario:
                - driving_experiment_name
                rcm:
                - model_id
                - rcm_version_id
                gcm:
                - driving_model_id
                gcm_ensemble_member:
                - driving_model_ensemble_member
                tracking-id_creation-date:
                - tracking_id
                - creation_date
                history-attribute:
                - history
                - history_of_appended_files
                input_frequency:
                - frequency
                input_institution:
                - institution
                input_institute_id:
                - institute_id
                input_references:
                - references
                input_product:
                - product
                input_contact:
                - contact
                input_software:
                - software
                input_project_id:
                - project_id
                CORDEX_domain:
                - CORDEX_domain

        output:
            create:
                institution: "Swedish Meteorological and Hydrological Institute, Rossby Centre"
                institute_id: SMHI
                references: "https://www.smhi.se/en/research/research-departments/climate-research-at-the-rossby-centre"
                creation_date: "{NOW}"
                software: "{GORDIAS_VERSION}"
                Conventions: "{CF_CONVENTIONS_VERSION}"
