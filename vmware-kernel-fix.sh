#!/bin/bash
# Fixes vmware error when recompiling the vmmon module with new kernel version
sudo CPATH=/usr/src/kernels/$(uname -r)/include/linux vmware-modconfig --console --install-all
