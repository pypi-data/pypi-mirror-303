# generated by duploctl pipeline, do no edit
class Duploctl < Formula

  desc "{description}"
  homepage "{repo_url}"
  version "{version}"
  license "MIT"
  base_url = "#{{homepage}}/releases/download/v#{{version}}"

  option "with-pip", "Use Brew PIP to install duploctl"

  if build.with? "pip"
    include Language::Python::Virtualenv
    url "#{{base_url}}/duplocloud_client-#{{version}}.tar.gz"
    sha256 "{pip_sha}"
    depends_on "python@3.12"
    {resources}
    def install
      virtualenv_install_with_resources
    end
  else
    on_macos do
      if Hardware::CPU.arm? && Hardware::CPU.is_64_bit?
        url "#{{base_url}}/duploctl-#{{version}}-darwin-arm64.tar.gz"
        sha256 "{macos_sha_arm64}"
      end
      if Hardware::CPU.intel?
        url "#{{base_url}}/duploctl-#{{version}}-darwin-amd64.tar.gz"
        sha256 "{macos_sha_amd64}"
      end
    end
  
    on_linux do
      if Hardware::CPU.arm? && Hardware::CPU.is_64_bit?
        url "#{{base_url}}/duploctl-#{{version}}-linux-arm64.tar.gz"
        sha256 "{linux_sha_arm64}"
      end
      if Hardware::CPU.intel?
        url "#{{base_url}}/duploctl-#{{version}}-linux-amd64.tar.gz"
        sha256 "{linux_sha_amd64}"
      end
    end
  
    def install
      bin.install "duploctl"
    end
  end

  test do
    system "duploctl --version"
  end
end
