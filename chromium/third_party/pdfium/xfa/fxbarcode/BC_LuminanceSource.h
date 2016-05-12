// Copyright 2014 PDFium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Original code copyright 2014 Foxit Software Inc. http://www.foxitsoftware.com

#ifndef XFA_FXBARCODE_BC_LUMINANCESOURCE_H_
#define XFA_FXBARCODE_BC_LUMINANCESOURCE_H_

#include "core/fxcrt/include/fx_basic.h"

class CBC_LuminanceSource {
 public:
  CBC_LuminanceSource(int32_t width, int32_t height);
  virtual ~CBC_LuminanceSource();
  int32_t GetWidth();
  int32_t GetHeight();

  virtual CFX_ByteArray* GetRow(int32_t y, CFX_ByteArray& row, int32_t& e) = 0;
  virtual CFX_ByteArray* GetMatrix() = 0;

 protected:
  int32_t m_width;
  int32_t m_height;
};

#endif  // XFA_FXBARCODE_BC_LUMINANCESOURCE_H_
