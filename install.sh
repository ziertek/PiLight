#!/usr/bin/sudo /bin/bash
SCRIPT=`realpath -s $0`
SCRIPTPATH=`dirname $SCRIPT`
STARTPWD=$PWD
GIT_URL='https://github.com/ziertek/PiLight'

# Define colors and styles
NORMAL="\033[0m"
BOLD="\033[1m"
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[93m"

show_msg() {
    echo -e $1 > /dev/tty
}

usage() {
    echo -e "${BOLD}Usage:${NORMAL}"
    echo -e "  -i  --install-dir        Specify where you want to install to"
    echo -e "                           Default is: ${BOLD}${SCRIPTPATH}${NORMAL}"
    echo -e "  -d  --development        Install for development only (no service installation)"
    echo -e "  -V  --verbose            Shows command output for debugging"
    echo -e "  -v  --version            Shows version details"
    echo -e "  -h  --help               Shows this usage message"
}

version() {
    echo -e "${BOLD}PiLight installation script 0.1${NORMAL}"
    echo -e "URL: $GIT_URL"
}

installSystemdService() {
    show_msg "${GREEN}Installing Systemd Service...${NORMAL}"
    sed -i "s+WorkingDirectory=/opt/PiLight+WorkingDirectory=$INSTALL_DIR+g" $INSTALL_DIR/PiLight.service
    if [[ ! -f /etc/systemd/system/PiLight.service ]]; then
        sudo cp PiLight.service /etc/systemd/system/PiLight.service
    else
        sudo sed -i "s+WorkingDirectory=/home/pi/unicorn-busy-server+WorkingDirectory=$INSTALL_DIR+g" /etc/systemd/system/PiLight.service
    fi
}

enableSystemdService() {
    show_msg "${GREEN}Starting Systemd Service...${NORMAL}"
    sudo systemctl enable PiLight.service
    sudo systemctl start PiLight.service
}


VERBOSE=false
DEVELOPMENT=false
INSTALL_DIR=$SCRIPTPATH
while [ "$1" != "" ]; do
    case $1 in
        -i | --install-dir)     shift
                                INSTALL_DIR=$1
                                ;;
        -d | --development)     DEVELOPMENT=true
                                ;;
        -V | --verbose)         VERBOSE=true
                                ;;
        -v | --version)         version
                                exit 0
                                ;;
        -h | --help)            version
                                echo -e ""
                                usage
                                exit 0
                                ;;
        * )                     echo -e "Unknown option $1...\n"
                                usage
                                exit 1
    esac
    shift
done

# Act on verbose option
if [ $VERBOSE == "false" ]; then
    exec > /dev/null 
fi

# Check if we have the required files or if we need to clone them
FILES=("server.py" "requirements.txt" "PiLight.service" "lib/__init__.py" "lib/phat_Wrapper.py" "lib/config.yaml")
FILECHECK=true
for FILE in ${FILES[@]}; do
    if [ $INSTALL_DIR != $SCRIPTPATH ]; then
        if [ $VERBOSE == "true" ]; then
            show_msg "Checking file... ${INSTALL_DIR}/${FILE}"
        fi
        if [ ! -f "${INSTALL_DIR}/${FILE}" ]; then
            FILECHECK=false
        fi
    else
        if [ $VERBOSE == "true" ]; then
            show_msg "Checking file... ${INSTALL_DIR}/${FILE}"
        fi
        if [ ! -f "${SCRIPTPATH}/${FILE}" ]; then
            FILECHECK=false
        fi
    fi
    if [ $FILECHECK == 'false' ]; then
        show_msg "${RED}The requried files are missing...${NORMAL} lets clone everything from git..."
        break
    fi
done

if [ $FILECHECK == 'false' ]; then
    which git > /dev/null
    if [[ $? != 0 ]]; then
        show_msg "${RED}git is not installed... please install git and run the script again!${NORMAL}"
        exit 1
    fi
    if [ "$(ls -A ${INSTALL_DIR})" ]; then
        INSTALL_DIR="$INSTALL_DIR/PiLight"
    fi
    show_msg "${GREEN}Cloning files from git using HTTPS to ${BOLD}${INSTALL_DIR}${NORMAL}${GREEN}...${NORMAL}"
    git clone -q $GIT_URL $INSTALL_DIR
    chown -R $SUDO_USER:$SUDO_USER $INSTALL_DIR
    cd $INSTALL_DIR
fi

case $(uname -s) in
    Linux|GNU*)     case $(lsb_release -si) in
                        Ubuntu | Raspbian)      show_msg "${GREEN}Installing required files from apt...${NORMAL}"
                                                sudo apt-get install -y python3-pip python3-dev
                                                show_msg "${GREEN}Installing needed files from pip...${NORMAL}"
                                                sudo pip3 install -r ./requirements.txt
                                                if [[ $DEVELOPMENT == "false" ]]; then
                                                    installSystemdService
                                                    enableSystemdService
                                                fi
                                                ;;
                        *)                      show_msg "${RED}${BOLD}Unsupported distribution, please consider submitting a pull request to extend the script${NORMAL}"
                                                exit 1
                    esac
                    ;;
    *)              show_msg "${RED}${BOLD}Unsupported operating system, please consider submitting a pull request to extend the script${NORMAL}"
                    exit 1
esac

# Change permissions of the start up script
sudo chmod +x Update/UpdatePi.sh
sudo chmod +x ./start.sh
cd $STARTPWD
show_msg "${GREEN}${BOLD}Installation complete${NORMAL}"