<div style="text-align: center; padding-bottom: 8px">
    <h1>gandula</h1>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Ball_boy.jpg/1200px-Ball_boy.jpg" alt="gandula" />
</div>

---

`gandula` is a specialized internal Python library developed by the Sports Analytics lab at the Federal University of Minas Gerais (UFMG). Designed to streamline our research efforts, `gandula` currently offers tools to help handling PFF data.

Gandula is the word for ball boy in brazilian portuguese. It originates from the 1930s, from the word "gandulo", that in archaic portuguese means slacker/beggar.
Back in the 30s, the word started to be used to refer to vagabond boys, who didn't nothing else to do but watch football in the pitches in Rio. These "gandulas"
would help by bringing the kicked out balls. In 1939, the Clube de Regatas Vasco da Gama hired the argentinian stricker Bernardo Gandulla, who was known to bring
back the ball as a fair play. The `gandula` then got popularized over the country. In our `gandula`, the ball is the data, and the data scientists/analysts are
the stars of the game.

---

## Quick Start
### Installation
In progress...


### Installation (for development)
To get started with `gandula`, follow these steps:

Clone the repository:
```bash
git clone git@github.com:SALabUFMG/gandula.git
cd gandula
```

Create and setup the environment. You can use python virtual environments or conda:
```bash
python3 -m venv .venv
source .venv/bin/activate
```
or:
```bash
conda create --prefix .venv python=3.10
conda activate ./.venv
```

After activating your environment, install uv
Install Poetry
```bash
pip install uv
```

Use uv to install the package:
```bash
uv pip install .
```

You're almost good to go. If you want to contribute, you'll also need to install pre-commit hooks that we use to keep the code clean.
Install pre-commit hooks:
```bash
pip install pre-commit
pre-commit install
```
Run the pre-commit before every commit
```bash
pre-commit run
```


### Setup

If you have access to the PFF API, you can use our `PFF_GQL_Client`. Create the file `.env` and add your `PFF_API_KEY` there:
```bash
PFF_API_KEY='YOUR_PFF_API_KEY'
```

If you don't have to the PFF API, but have acess to the data as json, you may want to use `PFF_JSON_Client`.

---

## Usage

We have notebooks that showcase how you can use the package.

- `pff-load-from-json.ipynb`: shows how to get event data using the JSON client.
- `pff-data-transformation.ipynb`: shows how to get data using the GQL client.
- `pff-defensive-line-height.ipynb`: gives example on how to use tracking data to define the defensive line of a team.
- `pff-search.ipynb`: gets video to watch a certain event.
- `pff-tracking.ipynb`: shows how to plot a video using tracking data.
- `pff-events-withing-tracking-to-pandas.ipynb`: passes events within the data into pandas.

---

## Development

For those looking to contribute to `gandula`, please ensure you have followed the installation steps under Quick Start. For more detailed information on setting up your development environment and contributing, refer to our contributing guidelines.


---

## License & Copyright

The main image is "Ballkid at soccer, China" by [Micah Sittig](https://www.flickr.com/photos/35468134321@N01), licensed under CC BY 2.0

