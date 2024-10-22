# CapibaraENT CLI

![Capibara SSBD Model](/src/public/capi33B2.webp)

CapibaraENT is a command-line tool for training, evaluating, and deploying Capibara-based language models, optimized for TPUs and featuring hyperparameter optimization.

## Features

- Training and evaluation of Capibara models
- Built-in TPU support
- Hyperparameter optimization
- Model deployment
- Performance measurement
- Docker container execution
- Model deserialization from JSON
- Integration with Weights & Biases for experiment tracking

## Requirements

- Python 3.7+
- PyTorch 1.8+
- PyTorch/XLA
- JAX (for TPU optimization)
- Weights & Biases
- Docker (optional, for container execution)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/capibaraent-cli.git
   cd capibaraent-cli
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up Weights & Biases:

   ```bash
   wandb login
   ```

## Usage

The CapibaraENT CLI offers various options for working with Capibara models:

```bash
python capibaraent_cli.py [options]

```

Available options:

- `--log-level`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `--train`: Train the model
- `--evaluate`: Evaluate the model
- `--optimize`: Perform hyperparameter optimization
- `--use-docker`: Run the model inside Docker
- `--deserialize-model`: Deserialize the model from JSON
- `--deploy`: Deploy the model
- `--measure-performance`: Measure the model's performance
- `--model`: Path to the model JSON file (for deserialization)

### Usage Examples

1. Train a model:

```bash
   python capibaraent_cli.py --train
 ```

Evaluate a model:

```bash
   python capibaraent_cli.py --evaluate
 ```

1. Perform hyperparameter optimization:

   ```bash
   python optimize_hyperparameters.py
   ```

2. Deploy a model:

   ```bash
   python capibaraent_cli.py --deploy
   ```

3. Measure model performance:

   ```bash
   python capibaraent_cli.py --measure-performance
   ```

4. Run a model in Docker:

   ```bash
   python capibaraent_cli.py --use-docker
   ```

5. Deserialize and run a model from JSON:

```bash
   python capibaraent_cli.py --deserialize-model --model model.json
```

## Configuration

Model configuration is handled through environment variables and the `.env` file. Key configuration parameters include:

- `CAPIBARA_LEARNING_RATE`
- `CAPIBARA_BATCH_SIZE`
- `CAPIBARA_MAX_LENGTH`
- `CAPIBARA_USE_TPU`
- `WANDB_PROJECT`
- `WANDB_ENTITY`

For a full list of configuration options, refer to the `.env.example` file.

## Hyperparameter Optimization

To perform hyperparameter optimization:

1. Ensure your Weights & Biases project is set up.
2. Run the optimization script:

   ```bash
   python optimize_hyperparameters.py
   ```

3. View the results in your Weights & Biases dashboard.

## Development

To contribute to the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Marco Durán - <marco@anachroni.co>

Project Link: [https://github.com/anachroni-io/capibaraent-cli](https://github.com/anachroni-io)

## Documentation

To generate the documentation:

 Install the required packages:

```bash
   pip install -r docs/requirements.txt
   ```

 Generate the HTML documentation:

```bash
   cd docs
   make html
   ```

 Open `docs/_build/html/index.html` in your web browser to view the documentation.
