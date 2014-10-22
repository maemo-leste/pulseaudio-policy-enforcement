# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       pulseaudio-policy-enforcement

# >> macros
# << macros

Summary:    Pulseaudio module for enforcing policy decisions in the audio domain
Version:    5.0.13
Release:    0
Group:      System/Daemons
License:    LGPLv2.1
URL:        https://github.com/nemomobile/pulseaudio-policy-enforcement
Source0:    %{name}-%{version}.tar.gz
Source100:  pulseaudio-policy-enforcement.yaml
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(pulsecore) >= 5.0
BuildRequires:  pkgconfig(libpulse) >= 5.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libmeego-common) >= 5.0.15
BuildRequires:  libtool-ltdl-devel

%description
This package contains a pulseaudio module that enforces (mostly audio) routing,
corking and muting policy decisions.


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
PAVER="`/usr/bin/pkg-config --silence-errors --modversion pulsecore | tr -d \\n | sed -e 's/\([0123456789.]\+\).*/\1/'`"
unset LD_AS_NEEDED
# << build pre

%autogen --disable-static
%configure --disable-static \
    --with-module-dir=%{_libdir}/pulse-$PAVER/modules

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post

# << install post

%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/pulse-*/modules/module-*.so
# << files