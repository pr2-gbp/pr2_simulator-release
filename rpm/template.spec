Name:           ros-melodic-pr2-gazebo-plugins
Version:        2.0.14
Release:        0%{?dist}
Summary:        ROS pr2_gazebo_plugins package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_gazebo_plugins
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-angles
Requires:       ros-melodic-cv-bridge
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-gazebo-msgs
Requires:       ros-melodic-gazebo-plugins
Requires:       ros-melodic-gazebo-ros
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-transport
Requires:       ros-melodic-message-generation
Requires:       ros-melodic-message-runtime
Requires:       ros-melodic-nav-msgs
Requires:       ros-melodic-orocos-kdl
Requires:       ros-melodic-polled-camera
Requires:       ros-melodic-pr2-controller-manager
Requires:       ros-melodic-pr2-hardware-interface
Requires:       ros-melodic-pr2-mechanism-model
Requires:       ros-melodic-pr2-msgs
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-rospy
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-tf
Requires:       ros-melodic-urdf
BuildRequires:  ros-melodic-angles
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-cv-bridge
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-gazebo-msgs
BuildRequires:  ros-melodic-gazebo-plugins
BuildRequires:  ros-melodic-geometry-msgs
BuildRequires:  ros-melodic-image-transport
BuildRequires:  ros-melodic-message-generation
BuildRequires:  ros-melodic-message-runtime
BuildRequires:  ros-melodic-nav-msgs
BuildRequires:  ros-melodic-orocos-kdl
BuildRequires:  ros-melodic-polled-camera
BuildRequires:  ros-melodic-pr2-controller-manager
BuildRequires:  ros-melodic-pr2-hardware-interface
BuildRequires:  ros-melodic-pr2-mechanism-model
BuildRequires:  ros-melodic-pr2-msgs
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-rospy
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf
BuildRequires:  ros-melodic-urdf

%description
Gazebo Plugins for various PR2-specific sensors and actuators on the robot.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Mon Apr 29 2019 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 2.0.14-0
- Autogenerated by Bloom

* Wed Apr 24 2019 ROS Orphaned Package Maintainers <ros-orphaned-packages@googlegroups.com> - 2.0.13-1
- Autogenerated by Bloom

