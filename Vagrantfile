# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure(2) do |config|

  # proxy config
  if Vagrant.has_plugin?("vagrant-proxyconf")
    config.proxy.http     = "http://87.254.212.121:8080"
    config.proxy.https    = "https://87.254.212.121:8080"
    config.proxy.no_proxy = "localhost,127.0.0.1"
  end

  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "ubuntu/trusty64"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8000, host: 8000
  config.vm.network "forwarded_port", guest: 8010, host: 8010
  config.vm.network "forwarded_port", guest: 5432, host: 5432

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  # config.vm.synced_folder "../data", "/vagrant_data"

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  # config.vm.provider "virtualbox" do |vb|
  #   # Display the VirtualBox GUI when booting the machine
  #   vb.gui = true
  #
  #   # Customize the amount of memory on the VM:
  #   vb.memory = "1024"
  # end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt-get update -y
    sudo apt-get install -y python-setuptools
    sudo apt-get install -y python-dev
    sudo apt-get install -y build-essential
    sudo apt-get install -y git
    sudo apt-get install -y sqlite
    sudo apt-get install -y vim
    sudo apt-get install -y pandoc
    sudo apt-get install -y postgresql
    sudo apt-get install -y postgresql-contrib
    sudo apt-get install -y libpq-dev
    sudo apt-get install -y libjpeg
    sudo apt-get install -y libjpeg-dev
    sudo apt-get install -y libfreetype6
    sudo apt-get install -y libfreetype6-dev
    sudo apt-get install -y zlib1g-dev
    sudo apt-get install -y libsasl2-dev
    sudo apt-get install -y libldap2-dev
    sudo apt-get install -y libssl-dev
    sudo apt-get install -y curl
    sudo apt-get install -y libatlas-base-dev
    sudo apt-get install -y gfortran
    sudo easy_install virtualenv
    sudo easy_install pip
    sudo easy_install virtualenvwrapper


    # config default programs
    curl -o /home/vagrant/.vimrc https://gist.githubusercontent.com/valdergallo/2979412/raw/84f99d85dcc7d89d38cb79ad58e1a08a99db58ad/vimrc
    curl -o /home/vagrant/.screenrc https://gist.githubusercontent.com/valdergallo/2979409/raw/59d3e9c14d417977bed5071c6226d55acf43cec6/screenrc
    curl -o /home/vagrant/.gitconfig https://gist.githubusercontent.com/valdergallo/3427676/raw/da8224e818d12fdbaa366747b92a02b25f2fa70d/.gitconfig
    mkdir -p /home/vagrant/.vim

    source /usr/local/bin/virtualenvwrapper.sh
    echo "source /usr/local/bin/virtualenvwrapper.sh " >> /home/vagrant/.bashrc
    echo "# Add these lines to the bottom of the file: " >> /home/vagrant/.bashrc
    echo "export LANGUAGE=en_US.UTF-8 " >> /home/vagrant/.bashrc
    echo "export LANG=en_US.UTF-8 " >> /home/vagrant/.bashrc
    echo "export LC_ALL=en_US.UTF-8 " >> /home/vagrant/.bashrc
    sudo locale-gen en_US.UTF-8
    sudo dpkg-reconfigure locales
    ln -s /vagrant work_home

    # listen for localhost connections
    export POSTGRE_VERSION=9.3
    sudo sed -i "s/#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/$POSTGRE_VERSION/main/postgresql.conf
    # identify users via "md5", rather than "ident", allowing us to make postgres
    # users separate from system users. "md5" lets us simply use a password
    echo "local   all             all                                     trust" | sudo tee -a /etc/postgresql/$POSTGRE_VERSION/main/pg_hba.conf
    echo "host    all             all             0.0.0.0/0               trust" | sudo tee -a /etc/postgresql/$POSTGRE_VERSION/main/pg_hba.conf

    # create new user "postgres" with defined password "postgres" not a superuser
    sudo -u postgres psql -c "CREATE ROLE postgres LOGIN UNENCRYPTED PASSWORD 'postgres' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;"

    sudo service postgresql start

  SHELL
end
