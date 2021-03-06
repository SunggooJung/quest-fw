# QUEST

## One-time setup:

You'll need the submodules and dependencies, so clone like so:
```
git clone --recurse-submodules REPO_ADDRESS
```

Or, after cloning, run:
```
git submodule update --init --recursive 
```

To get the F’ dependencies on Ubuntu (all dependencies are available through Homebrew on Mac):
```
sudo apt-get install pkg-config g++ python-pip python-lxml python-tk python-dev
```

On all platforms (modify the pip command if you don’t want a global install)
```
sudo -H pip install -r Gse/bin/required.txt
```

## Using with ROS (needed for `SIMREF` and `SDREF`)

Go to the ROS/fprime_ws folder, and build the workspace with your ROS environment sourced (tested with catkin):
```
catkin init
catkin build
```

## Using without ROS
From the top directory of the repo, run:
```
touch ROS/fprime_ws/src/fprime/mod.mk
```

## Installing command dictionaries
For a particular deployment (e.g. `SDREF`, `HEXREF`), go to that folder and run `make dict_install`

Then, run `touch Gse/generated/DEPLOYMENT/serializable/ROS/__init__.py`
See https://github.com/genemerewether/quest-fw/issues/3

## `SDREF`: High-level processor deployment

- Acts as a shim to transport data to and from low-level processor
- Interfaces with ROS and F' ground station
- On Snapdragon Flight, loads `HEXREF` onto DSP and interfaces with that code
- On any Linux environment, interfaces to low-level processor over two UARTS (one data and one debug)

To set up a new installation, download `Flight_3.1.3_qrlSDK.tgz` from Intrinsyc and `qualcomm_hexagon_sdk_lnx_3_0_eval.bin` from Qualcomm, and place in `cross_toolchain/downloads`.

Run `./bootstrap.bash` from the top level of the repository. This will set up the Hexagon toolchain using `install.sh` from `cross_toolchain`, install all required dependencies, create a Linaro Indigo ARM sysroot and install ROS in it using `proot` for later cross-compilation include and link steps.

## `R5REF`: TI TMS570 deployment

Tested on Linux and Mac with TI Code Composer Studio version `8.1.0`, with ARM compiler version `18.1.2`

## `SIMREF`: Simulation deployment (works with RotorS from ETH)

To build the simulation example, go to the SIMREF folder, and run the following:
```
make gen_make
make
```

Then, you can run the executable like so (after starting ROS master):
```
ROS_NAMESPACE=firefly ./linux-linux-x86-debug-gnu-bin/SIMREF
```

When you start the RotorS (https://github.com/ethz-asl/rotors_simulator) firefly example, SIMREF will use the /clock message to carry out control cycles. This parallels what happens on hardware targets, where the IMU data-ready interrupt triggers the estimation and control loops.

Works out of the box with https://github.com/genemerewether/ethzasl_sensor_fusion for testing high-level filter updates, but can be easily adapted to simulated sensors in Gazebo. Just run additional ROS nodes as necessary, and remap the pose or position sensor topics of the sensor fusion packages. Or, publish the `mav_msgs/ImuStateUpdate` message (see the `mav_msgs` submodule of this repo) from an appropriate filter.

# fprime

F' Release Notes

Release 1.0: 

This is the initial release of the software to open source. See the license file for terms of use.

An architectural overview of the software can be found [here.](docs/Architecture/FPrimeArchitectureShort.pdf)

A user's guide can be found [here.](docs/UsersGuide/FprimeUserGuide.pdf)
   
Documentation for the Reference example can be found [here.](Ref/docs/sdd.md)

Release 1.01

Updated contributor list. No code changes. 
