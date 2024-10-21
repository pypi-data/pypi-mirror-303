# Changelog

All notable changes to this project will be documented in this file. See [conventional commits](https://www.conventionalcommits.org/) for commit guidelines.

## [0.3.0](https://github.com/imbus/robotframework-PlatynUI/compare/v0.2.0..v0.3.0) - 2024-10-21

### Bug Fixes

- Use os.name instead of platform.platform ([7e962f0](https://github.com/imbus/robotframework-PlatynUI/commit/7e962f0b4f5802e548396c051754de29c15b5b8c))


### Features

- Added first version of the common adapter factory and adapter implementation ([6171b97](https://github.com/imbus/robotframework-PlatynUI/commit/6171b97b8cdafd0cddac47fb75580ee76efcecd8))
- Introduce a provider folder and put the avalonia provider into it ([7375295](https://github.com/imbus/robotframework-PlatynUI/commit/737529544ceaea7389dcdc3f66f6646557889e62))
- Add cli to call PlatynUI.Spy ([4ee9a4d](https://github.com/imbus/robotframework-PlatynUI/commit/4ee9a4d4fe89fe738e9e71619accfde9e35fadd6))
- Make PlatynUI.Spy starting on windows ([9312eb7](https://github.com/imbus/robotframework-PlatynUI/commit/9312eb75535b3b55866f02acbdf2122ebac5a285))


### Refactor

- Fix some imports ([90ec684](https://github.com/imbus/robotframework-PlatynUI/commit/90ec6840562d5dd4f28bbfa2957b46950e296e44))


## [0.2.0](https://github.com/imbus/robotframework-PlatynUI/compare/v0.1.0..v0.2.0) - 2024-10-18

### Bug Fixes

- **Spy:** Some correction theming for different platforms ([5c60486](https://github.com/imbus/robotframework-PlatynUI/commit/5c604867abe107e71c5bdcad8ed1272fea4691a2))
- **Spy:** Some correction for the new logo ([1a20c30](https://github.com/imbus/robotframework-PlatynUI/commit/1a20c306d847eed42abdc27f2317f60ebd21ed69))
- **spy:** Some customizations for linux ([bd86355](https://github.com/imbus/robotframework-PlatynUI/commit/bd863557c0d9fc8dec3766912bcb20762a97f808))
- Corrected flickering of datagrid in spy ([0511704](https://github.com/imbus/robotframework-PlatynUI/commit/05117041bb8ccd37687ef95afb3f2412e85e704c))
- Correct comparing assembly names at loading platform specific parts ([61eaa39](https://github.com/imbus/robotframework-PlatynUI/commit/61eaa398829f7019081b9b2a189de88e4757f43f))
- BoundingRectangle now gives the correct values ([b8ec1a7](https://github.com/imbus/robotframework-PlatynUI/commit/b8ec1a7268e2b883bffb7a55383e8928fe168df5))


### Features

- **Spy:** Be more fluent and define cancel and refresh keybinding ([b9f05c6](https://github.com/imbus/robotframework-PlatynUI/commit/b9f05c6fb4be56bceec3d3b7129c65ab26079ed2))
- **spy:** Add a new window icon ([b39bd9f](https://github.com/imbus/robotframework-PlatynUI/commit/b39bd9f6e346b7a89adfbec870c24b52dcb16c5f))
- Start implementing a platform-independent spy tool ([46d811c](https://github.com/imbus/robotframework-PlatynUI/commit/46d811c6a5cda5590af45e0aa3fde133fef6d33c))
- Search for elements in PlatynUI.Spy using XPath ([051b250](https://github.com/imbus/robotframework-PlatynUI/commit/051b25054e450452ba6b6b3c648855aa446f8ac7))
- Highlighter for Win32 ([d032d9f](https://github.com/imbus/robotframework-PlatynUI/commit/d032d9f272238e93659d16b212c8e04d6068ff67))
- Introduce Semi.Avalonia theme for spy ([f601db7](https://github.com/imbus/robotframework-PlatynUI/commit/f601db7b27344347285b08a8084efdc859fb168b))
- Switch to FluentAvaloniaUI theme ([ae4657a](https://github.com/imbus/robotframework-PlatynUI/commit/ae4657a826ea6459bf163559d5658d153cb2d5b2))
- ApplicationNodes for UIAutomation ([0aa677d](https://github.com/imbus/robotframework-PlatynUI/commit/0aa677d5c85c77c87534c88b535c3318676f75bc))
- Show attributes in spy as a c# expression ([28a743d](https://github.com/imbus/robotframework-PlatynUI/commit/28a743d87f755aa03baad18ecec2be5e865103f4))
- First X11 Desktop support ([3e42cc1](https://github.com/imbus/robotframework-PlatynUI/commit/3e42cc1a651a0338d47732e0d1ffbb79eae86574))
- Simple highlighter for X11 ([42df0ca](https://github.com/imbus/robotframework-PlatynUI/commit/42df0ca5837b8450cb4d1755a155901222b68188))
- Implement some operators for PlatynUI.Runtime.Types ([e204eec](https://github.com/imbus/robotframework-PlatynUI/commit/e204eecfb4e586426f304fba96dc15811c4694cd))
- First version of at-spi2 extension ([6330edc](https://github.com/imbus/robotframework-PlatynUI/commit/6330edc7e5029a72f4b8a2540ce932b68fb14620))
- First version that connects to an avalonia app ([9e3bc45](https://github.com/imbus/robotframework-PlatynUI/commit/9e3bc451c8a752a13709a8be3415bd0c08284e65))
- First version of showing avalonia controls ([18da5c8](https://github.com/imbus/robotframework-PlatynUI/commit/18da5c824db79a58edc4fb83c6d59634602bf5a3))
- Add nativeand clr properties to Avalonia provider ([c091c1b](https://github.com/imbus/robotframework-PlatynUI/commit/c091c1b1697d5b33b8c8355e66820970f33b1a04))
- Optimize highlighter for X11 ([9911f5a](https://github.com/imbus/robotframework-PlatynUI/commit/9911f5a7655f98857a257c934d6a310f558f177e))
- Show some more attributes for at-spi2 ([9b7e37a](https://github.com/imbus/robotframework-PlatynUI/commit/9b7e37acc5c976943998fc8539dad8faf0b088b7))
- Implement IElement for UIAutomationElement ([323c1e4](https://github.com/imbus/robotframework-PlatynUI/commit/323c1e440c8cc44d19c4737941d45c3b34851355))
- Mouse and keyboard device for win32 ([b177496](https://github.com/imbus/robotframework-PlatynUI/commit/b177496453bb7ad9b5e239608f46c0530fc5610f))
- Implement devices for python ([74c003f](https://github.com/imbus/robotframework-PlatynUI/commit/74c003fc830940ce3e3db4e24a7f7cb8a0374842))
- Connect devices to DefaultTechnology ([6b64ad6](https://github.com/imbus/robotframework-PlatynUI/commit/6b64ad68f8c9ca7fff937701c0e85b85d7d5d3b8))


### Refactor

- User own hatch custom hook to build dotnet packages ([fa11f97](https://github.com/imbus/robotframework-PlatynUI/commit/fa11f97c9530b9c8fc2dc1d1291e33c18238be6e))
- Rename some packages ([35d54c4](https://github.com/imbus/robotframework-PlatynUI/commit/35d54c4d3d9f3428d33a9d5decf2d8f9b262c455))


## [0.1.0] - 2024-07-18

### Features

- **Spy:** Add tooltip to search results with full path of the element ([a54d667](https://github.com/imbus/robotframework-PlatynUI/commit/a54d66787dff2efb8351ffbc704eb8db63a2458f))
- **uiautomation:** Implement basic adapters and mouse device ([9e4612d](https://github.com/imbus/robotframework-PlatynUI/commit/9e4612d1ce79cbc34ae1466f38a23aa4fcdadf8e))
- Implement roundtrip for mouse, keyboard, focus, etc. handling ([fa9b235](https://github.com/imbus/robotframework-PlatynUI/commit/fa9b235cb2c5d9533c8cca6f0e8c1811da48ffd4))
- Implement highlighter ([08e01ff](https://github.com/imbus/robotframework-PlatynUI/commit/08e01ff1b1bb63cf206cf8406f01e8ea4a4ffea5))
- Add uiautomation spy/viewer ([2164320](https://github.com/imbus/robotframework-PlatynUI/commit/216432058b3f1dcc910f0ff2748a2ba4d0c04993))
- Add start script for `PlatynUI.UiAutomation.Spy` ([1f060c0](https://github.com/imbus/robotframework-PlatynUI/commit/1f060c071fa1732b0d4efd9052f8d4a953a7ad2d))
- Use different runtimes for coreclr and netfx ([59d1b2b](https://github.com/imbus/robotframework-PlatynUI/commit/59d1b2b18a7173fc4511f50954a527a53beaa3a6))
- Implement keyboard keywords ([0eaad09](https://github.com/imbus/robotframework-PlatynUI/commit/0eaad098133bf294608b852819afbf69356f3f24))
- Implement `ensure_exists` keyword ([b725110](https://github.com/imbus/robotframework-PlatynUI/commit/b725110f201204698e3af7cadbfaae94aeb220e7))


### Refactor

- Optimized enumerating child elements ([8b89143](https://github.com/imbus/robotframework-PlatynUI/commit/8b891437d27215dc7b52d96e1b60bf395f0d11b4))
- Some refactorings in spy ([eb83e89](https://github.com/imbus/robotframework-PlatynUI/commit/eb83e89d2b5e50ec4b4406c715e5650f6f1e3f56))
- Some refactorings ([bf44326](https://github.com/imbus/robotframework-PlatynUI/commit/bf44326da986077ec7ad944c859113ce86a23ce9))
- XPathNavigator reworked and optimized ([9691f7d](https://github.com/imbus/robotframework-PlatynUI/commit/9691f7dde8b9fb55b27499b2965fc5073533a238))


### Testing

- Add wpf test application ([1385331](https://github.com/imbus/robotframework-PlatynUI/commit/1385331260f022a45328cc2f7921d7cf144beab4))
- Simplified WpfTestApp ([df3a2d8](https://github.com/imbus/robotframework-PlatynUI/commit/df3a2d8d9efe347f33f020299b98a405e817553e))


<!-- generated by git-cliff -->
