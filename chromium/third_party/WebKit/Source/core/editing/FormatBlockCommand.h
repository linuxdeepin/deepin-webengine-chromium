/*
 * Copyright (C) 2006, 2008 Apple Inc. All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY APPLE COMPUTER, INC. ``AS IS'' AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 * PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL APPLE COMPUTER, INC. OR
 * CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 * EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
 * PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
 * PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
 * OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#ifndef FormatBlockCommand_h
#define FormatBlockCommand_h

#include "core/dom/Position.h"
#include "core/dom/QualifiedName.h"
#include "core/editing/ApplyBlockElementCommand.h"
#include "core/editing/EditAction.h"

namespace blink {

class Document;
class Element;
class Range;
class VisiblePosition;

class FormatBlockCommand final : public ApplyBlockElementCommand {
public:
    static PassRefPtrWillBeRawPtr<FormatBlockCommand> create(Document& document, const QualifiedName& tagName)
    {
        return adoptRefWillBeNoop(new FormatBlockCommand(document, tagName));
    }

    virtual bool preservesTypingStyle() const override { return true; }

    static Element* elementForFormatBlockCommand(Range*);
    bool didApply() const { return m_didApply; }

private:
    FormatBlockCommand(Document&, const QualifiedName& tagName);

    virtual void formatSelection(const VisiblePosition& startOfSelection, const VisiblePosition& endOfSelection) override;
    virtual void formatRange(const Position& start, const Position& end, const Position& endOfSelection, RefPtrWillBeRawPtr<HTMLElement>&) override;
    virtual EditAction editingAction() const override { return EditActionFormatBlock; }

    bool m_didApply;
};

} // namespace blink

#endif // FormatBlockCommand_h
