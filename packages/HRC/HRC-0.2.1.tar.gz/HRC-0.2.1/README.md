# HRC

HRC is a Python library designed for controll of HRC Hand designed and manufactured by Faculty of Technical Sciences Novi Sad.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install HRC.

```bash
pip install HRC
```

## Usage

```python
import HRC

# make an instance of HRC hand
my_hand = HRC.HRC_Hand()

# set finger's velocity
my_hand.finger_1.set_desired_speed(30)

# set finger's torque
my_hand.finger_2.set_desired_torque(2000)

# move finger for desired amount
my_hand.thumb_flexion.rotate(theta = 172, speed = 50, torque = 3000)
```

## License

[FTN Novi Sad]