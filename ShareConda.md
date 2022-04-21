## Share your conda env

There may come a time where you want to share the contents of your Conda environment.

This could be to share a project workflow with a colleague or with someone else who's trying to set up their system to have access to the same tools as yours.

There a couple of ways to do this:

1. Share your entire project folder (including the environment folder containing all of your Conda packages).

2. Share a .yml (pronounced YAM-L) file of your Conda environment.

The benefit of 1 is it's a very simple setup, share the folder, activate the environment, run the code. However, an environment folder can be quite a large file to share.

That's where 2 comes in. A .yml is basically a text file with instructions to tell Conda how to set up an environment.

For example, to export the environment we created earlier at /Users/daniel/Desktop/project_1/env as a YAML file called environment.yml we can use the command:

conda env export --prefix /Users/daniel/Desktop/project_1/env > environment.yml

After running the export command, we can see our new .yml file stored as environment.yml.

A sample .yml file might look like the following:

name: my_ml_env
dependencies:
  - numpy
  - pandas
  - scikit-learn
  - jupyter
  - matplotlib
Of course, your actual file will depend on the packages you've installed in your environment.

For more on sharing an environment, check out the Conda documentation on sharing environments.

Finally, to create an environment called env_from_file from a .yml file called environment.yml, you can run the command:

conda env create --file environment.yml --name env_from_file

For more on creating an environment from a .yml file, check out the Conda documentation on creating an environment from a .yml file.



PS Thank you to Konstantin for pointing this out.