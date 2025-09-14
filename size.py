import os
import sys
import site

def get_package_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            try:
                fp = os.path.join(dirpath, f)
                if os.path.isfile(fp):
                    total_size += os.path.getsize(fp)
            except OSError:
                pass
    return total_size

def main():
    # Find the site-packages directory
    site_packages_dirs = site.getsitepackages() if hasattr(site, "getsitepackages") else [site.getusersitepackages()]
    package_sizes = []

    for site_dir in site_packages_dirs:
        if not os.path.isdir(site_dir):
            continue
        for item in os.listdir(site_dir):
            item_path = os.path.join(site_dir, item)
            if os.path.isdir(item_path):
                size_mb = get_package_size(item_path) / (1024 * 1024)
                package_sizes.append((item, size_mb))

    # Sort from largest to smallest
    package_sizes.sort(key=lambda x: x[1], reverse=True)

    # Print results
    print(f"{'Package':<40} {'Size (MB)':>10}")
    print("-" * 52)
    for name, size in package_sizes:
        print(f"{name:<40} {size:>10.2f}")

if __name__ == "__main__":
    main()
