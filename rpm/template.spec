Name:           ros-melodic-pr2-gazebo
Version:        2.0.14
Release:        0%{?dist}
Summary:        ROS pr2_gazebo package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_gazebo
Source0:        %{name}-%{version}.tar.gz

Requires:       gazebo-devel
Requires:       ros-melodic-diagnostic-aggregator
Requires:       ros-melodic-fingertip-pressure
Requires:       ros-melodic-gazebo-plugins
Requires:       ros-melodic-gazebo-ros
Requires:       ros-melodic-geometry-msgs
Requires:       ros-melodic-image-proc
Requires:       ros-melodic-joint-trajectory-action
Requires:       ros-melodic-pr2-controller-configuration-gazebo
Requires:       ros-melodic-pr2-controller-manager
Requires:       ros-melodic-pr2-dashboard-aggregator
Requires:       ros-melodic-pr2-description
Requires:       ros-melodic-pr2-gazebo-plugins
Requires:       ros-melodic-pr2-gripper-action
Requires:       ros-melodic-pr2-head-action
Requires:       ros-melodic-pr2-mechanism-controllers
Requires:       ros-melodic-pr2-msgs
Requires:       ros-melodic-robot-mechanism-controllers
Requires:       ros-melodic-robot-pose-ekf
Requires:       ros-melodic-robot-state-publisher
Requires:       ros-melodic-rospy
Requires:       ros-melodic-rostopic
Requires:       ros-melodic-single-joint-position-action
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-stereo-image-proc
Requires:       ros-melodic-tf2-ros
Requires:       ros-melodic-topic-tools
Requires:       ros-melodic-xacro
BuildRequires:  gazebo-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-gazebo-plugins
BuildRequires:  ros-melodic-pr2-gazebo-plugins
BuildRequires:  ros-melodic-pr2-machine
BuildRequires:  ros-melodic-pr2-tuckarm
BuildRequires:  ros-melodic-rostest

%description
Launch scripts for simulating the PR2 in gazebo. The simulation equivalent of
pr2.launch is found here. pr2_fingertip_pressure_contact_translator produces the
same ROS topics as fingertip_pressure package for simulated PR2.

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

