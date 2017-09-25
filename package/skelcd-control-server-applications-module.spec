#
# spec file for package skelcd-control-server-applications-module
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-server-applications-module repository
#
#   See https://github.com/yast/skelcd-control-server-applications-module/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-server-applications-module
# xmllint (for validation)
BuildRequires:  libxml2-tools
# RNG validation schema
BuildRequires:  yast2-installation-control >= 4.0.0

Url:            https://github.com/yast/skelcd-control-server-applications-module
AutoReqProv:    off
Version:        15.0.0
Release:        0
Summary:        Server Application module roles definition
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2
Provides:       installer_module_extension() = server-application

%description
Meta package for Server Application module roles definition.
It is not intended for installation.

%prep

%setup -n %{name}-%{version}

%check
#
# Verify syntax
#
make -C control check

%install

mkdir -p $RPM_BUILD_ROOT
#
# Add control file
#
install -m 644 control/installation.xml $RPM_BUILD_ROOT/

# install LICENSE (required by build service check)
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}
install -m 644 LICENSE $RPM_BUILD_ROOT/%{_prefix}/share/doc/packages/%{name}

%files
%defattr(644,root,root,755)
/installation.xml
%doc %dir %{_prefix}/share/doc/packages/%{name}
%doc %{_prefix}/share/doc/packages/%{name}/LICENSE

%changelog
