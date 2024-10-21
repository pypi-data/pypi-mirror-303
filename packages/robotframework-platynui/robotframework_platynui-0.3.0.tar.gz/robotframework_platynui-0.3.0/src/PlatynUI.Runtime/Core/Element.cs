// SPDX-FileCopyrightText: 2024 Daniel Biehl <daniel.biehl@imbus.de>
//
// SPDX-License-Identifier: Apache-2.0

namespace PlatynUI.Runtime.Core;

public interface IElement
{
    bool IsEnabled { get; }
    bool IsVisible { get; }
    bool IsInView { get; }
    bool TopLevelParentIsActive { get; }
    Rect BoundingRectangle { get; }
    Rect VisibleRectangle { get; }
    Point? DefaultClickPosition { get; }

    bool TryEnsureVisible();
    bool TryEnsureApplicationIsReady();
    bool TryEnsureToplevelParentIsActive();
    bool TryBringIntoView();
}
