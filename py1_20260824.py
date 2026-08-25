"""Quick check for common Python data-analysis packages."""

from importlib import import_module


PACKAGES = [
	("numpy", "NumPy"),
	("pandas", "pandas"),
	("matplotlib", "Matplotlib"),
	("seaborn", "Seaborn"),
	("scipy", "SciPy"),
	("sklearn", "scikit-learn"),
]


def check_packages():
	print("Checking data-analysis packages...\n")
	imported = {}

	for module_name, package_name in PACKAGES:
		try:
			module = import_module(module_name)
			version = getattr(module, "__version__", "version unavailable")
			imported[module_name] = module
			print(f"[OK]     {package_name}: {version}")
		except ImportError as error:
			print(f"[MISSING] {package_name}: {error}")

	if "numpy" in imported and "pandas" in imported:
		import numpy as np
		import pandas as pd

		data = pd.DataFrame({"value": np.arange(1, 6)})
		print("\nSample pandas DataFrame:")
		print(data)
		print(f"Mean: {data['value'].mean()}")

	print("\nCheck complete.")
	print("Install missing packages with: python -m pip install numpy pandas matplotlib seaborn scipy scikit-learn")


if __name__ == "__main__":
	check_packages()
