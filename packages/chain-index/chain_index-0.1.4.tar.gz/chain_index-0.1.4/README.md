
## API Reference

### `get_chain_info(chain_identifier: Union[int, str]) -> ChainInfo`

Retrieves chain information based on the provided identifier.

- `chain_identifier`: Can be an integer (chain ID) or a string (chain name or alias)
- Returns a `ChainInfo` object containing chain details
- Raises `ChainNotFoundError` if the chain is not found

### `ChainInfo`

A Pydantic model representing chain information. Key attributes include:

- `name`: Chain name
- `chainId`: Chain ID
- `nativeCurrency`: Native currency details (name, symbol, decimals)
- `wrapperNativeCurrency`: Wrapper native currency details (name, symbol, decimals, contract)
- `rpc`: List of RPC URLs
- `explorers`: List of block explorers

## Development

To set up the development environment:

1. Clone the repository
2. Install development dependencies: `pip install -e ".[dev]"`
3. Run tests: `pytest`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project uses data from the [chainid.network](https://chainid.network/) project, which provides a comprehensive list of EVM-compatible chains.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for a detailed history of changes to this project.

## Authors

- gmatrix - Initial work and maintenance

## Disclaimer

This package is provided as-is, and while we strive for accuracy, we cannot guarantee the correctness of all chain information. Users should verify critical information independently.