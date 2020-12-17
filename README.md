
# Data, code, and materials for "The influence of long-term memory on working memory: Age-differences in proactive facilitation and interference"

Pre-print here: https://psyarxiv.com/gyjtz

## Data/Code

`data/` contains all of the raw data files from pavlovia, with separate folders for the different distraction and interval conditions. Each subfolder has an `R` script (`read-...R`) that combines data sets from a particular condition and the `combine-datasets.R` script puts everything together. All of the combined datasets are included in the repository already so there is no need to run these scripts (other than to check our way of reading in the data).

`analysis/` contains the functions and analysis script used to run the analyses reported in the paper. The resulting `.rds` files are too big to be uploaded to github so you can either run the models or download the fitted `brms` model objects from [here](https://drive.google.com/drive/folders/1paIh37hG58P-59YqJll7zhfvO-JD1jCJ?usp=sharing).

## Materials

Psychopy tasks and materials can be downloaded from the following gitlab/pavlovia repositories:
- [2 second interval, no distraction](https://gitlab.pavlovia.org/buchsbaumlab/proactive)
- [2 second interval, with distraction](https://gitlab.pavlovia.org/buchsbaumlab/proactive2)
- [10 second interval, no distraction](https://gitlab.pavlovia.org/buchsbaumlab/proactive3-2)
- [10 second interval, with distraction](https://gitlab.pavlovia.org/buchsbaumlab/proactive3-1)
