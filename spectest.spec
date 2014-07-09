#
# spec file for package spectest
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Mitsutoshi NAKANO <bkbin005@rinku.zaq.ne.jp>
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines

Name:           spectest
Version:        0
Release:        0
Summary:        Test spec file
License:        SUSE-Public-Domain
Group:          System/Management
Url:            http://github.com/MItsutoshiNAKANO/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       %{name}-vc

%description
Test spec file.
Please see Also:
http://lists.opensuse.org/archive/opensuse-factory/2014-07/msg00061.html
http://lists.opensuse.org/archive/opensuse-factory/2014-07/msg00063.html

%package git
Summary:        The git stub
Group:          System/Management
Requires:       git
Provides:       %{name}-vc

%description git
The git stub.
Please see Also:
http://lists.opensuse.org/archive/opensuse-factory/2014-07/msg00061.html
http://lists.opensuse.org/archive/opensuse-factory/2014-07/msg00063.html


%package bzr
Summary:        The bzr stub
Group:          System/Management
Requires:       bzr
Provides:       %{name}-vc

%description bzr
The bzr stub.
Please see Also:
http://lists.opensuse.org/archive/opensuse-factory/2014-07/msg00061.html
http://lists.opensuse.org/archive/opensuse-factory/2014-07/msg00063.html


%prep
%setup -q

%build

%install

%files
%defattr(-,root,root)
%doc README

%files git
%defattr(-,root,root)

%files bzr
%defattr(-,root,root)

%changelog
