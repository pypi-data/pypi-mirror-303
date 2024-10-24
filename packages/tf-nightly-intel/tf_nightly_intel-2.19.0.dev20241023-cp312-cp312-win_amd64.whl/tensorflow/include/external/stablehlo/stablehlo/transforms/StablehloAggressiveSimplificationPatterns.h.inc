/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Rewriters                                                                  *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|* From: StablehloAggressiveSimplificationPatterns.td                         *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/


static ::llvm::LogicalResult __mlir_ods_local_type_constraint_StablehloAggressiveSimplificationPatterns1(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Type type,
    ::llvm::StringRef failureStr) {
  if (!((((::llvm::isa<::mlir::RankedTensorType>(type))) && ((::llvm::cast<::mlir::ShapedType>(type).hasStaticShape()))) && ([](::mlir::Type elementType) { return (true); }(::llvm::cast<::mlir::ShapedType>(type).getElementType())))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": statically shaped tensor of any type values";
    });
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult __mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns1(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Attribute attr,
    ::llvm::StringRef failureStr) {
  if (!((::mlir::matchPattern(attr, m_AnyAttrOf(m_Zero(), m_AnyZeroFloat()))))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": is int or float zero";
    });
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult __mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns2(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Attribute attr,
    ::llvm::StringRef failureStr) {
  if (!((::mlir::matchPattern(attr, m_Zero())))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": is integer zero";
    });
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult __mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns3(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Attribute attr,
    ::llvm::StringRef failureStr) {
  if (!((::mlir::matchPattern(attr, m_One())))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": is integer one";
    });
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult __mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns4(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Attribute attr,
    ::llvm::StringRef failureStr) {
  if (!((isIotaRange(cast<DenseI64ArrayAttr>(attr).asArrayRef())))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": is iota dimensions";
    });
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult __mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns5(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Attribute attr,
    ::llvm::StringRef failureStr) {
  if (!((llvm::is_sorted(cast<DenseI64ArrayAttr>(attr).asArrayRef())))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": is sorted dimensions";
    });
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult __mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns6(
    ::mlir::PatternRewriter &rewriter, ::mlir::Operation *op, ::mlir::Attribute attr,
    ::llvm::StringRef failureStr) {
  if (!((cast<DenseI64ArrayAttr>(attr).empty()))) {
    return rewriter.notifyMatchFailure(op, [&](::mlir::Diagnostic &diag) {
      diag << failureStr << ": is empty i64 array";
    });
  }
  return ::mlir::success();
}
static ::llvm::LogicalResult static_dag_matcher_0(::mlir::PatternRewriter &rewriter, ::mlir::Operation *op0, ::llvm::SmallVector<::mlir::Operation *, 4> &tblgen_ops, ::mlir::stablehlo::ConstantOp &lhs, ::mlir::ElementsAttr &value) {
  (void)tblgen_ops;
  auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ConstantOp>(op0); (void)castedOp1;
  if (!(castedOp1)){
    return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
      diag << "castedOp1 is not ::mlir::stablehlo::ConstantOp type";
    });
  }
  lhs = castedOp1;
  {
    auto tblgen_attr = op0->getAttrOfType<::mlir::ElementsAttr>("value");(void)tblgen_attr;
    if (!(tblgen_attr)){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "expected op 'stablehlo.constant' to have attribute 'value' of type '::mlir::ElementsAttr'";
      });
    }
    value = tblgen_attr;
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult static_dag_matcher_1(::mlir::PatternRewriter &rewriter, ::mlir::Operation *op0, ::llvm::SmallVector<::mlir::Operation *, 4> &tblgen_ops, ::mlir::stablehlo::ConstantOp &zero, ::mlir::ElementsAttr &value) {
  (void)tblgen_ops;
  auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ConstantOp>(op0); (void)castedOp1;
  if (!(castedOp1)){
    return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
      diag << "castedOp1 is not ::mlir::stablehlo::ConstantOp type";
    });
  }
  zero = castedOp1;
  {
    auto tblgen_attr = op0->getAttrOfType<::mlir::ElementsAttr>("value");(void)tblgen_attr;
    if (!(tblgen_attr)){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "expected op 'stablehlo.constant' to have attribute 'value' of type '::mlir::ElementsAttr'";
      });
    }
    if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns2(rewriter, op0, tblgen_attr, "op 'stablehlo.constant' attribute 'value' failed to satisfy constraint: 'is integer zero'"))) {
      return ::mlir::failure();
    }
    value = tblgen_attr;
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult static_dag_matcher_2(::mlir::PatternRewriter &rewriter, ::mlir::Operation *op0, ::llvm::SmallVector<::mlir::Operation *, 4> &tblgen_ops, ::mlir::stablehlo::ConstantOp &one, ::mlir::ElementsAttr &value) {
  (void)tblgen_ops;
  auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ConstantOp>(op0); (void)castedOp1;
  if (!(castedOp1)){
    return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
      diag << "castedOp1 is not ::mlir::stablehlo::ConstantOp type";
    });
  }
  one = castedOp1;
  {
    auto tblgen_attr = op0->getAttrOfType<::mlir::ElementsAttr>("value");(void)tblgen_attr;
    if (!(tblgen_attr)){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "expected op 'stablehlo.constant' to have attribute 'value' of type '::mlir::ElementsAttr'";
      });
    }
    if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns3(rewriter, op0, tblgen_attr, "op 'stablehlo.constant' attribute 'value' failed to satisfy constraint: 'is integer one'"))) {
      return ::mlir::failure();
    }
    value = tblgen_attr;
  }
  return ::mlir::success();
}

static ::llvm::LogicalResult static_dag_matcher_3(::mlir::PatternRewriter &rewriter, ::mlir::Operation *op0, ::llvm::SmallVector<::mlir::Operation *, 4> &tblgen_ops, ::mlir::Operation::operand_range &lhs, ::mlir::Operation::operand_range &rhs) {
  (void)tblgen_ops;
  auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ComplexOp>(op0); (void)castedOp1;
  if (!(castedOp1)){
    return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
      diag << "castedOp1 is not ::mlir::stablehlo::ComplexOp type";
    });
  }
  lhs = castedOp1.getODSOperands(0);
  rhs = castedOp1.getODSOperands(1);
  return ::mlir::success();
}

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:87
*/
struct GeneratedConvert0 : public ::mlir::RewritePattern {
  GeneratedConvert0(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.add", 2, context, {"stablehlo.add"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::AddOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::AddOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::AddOp tblgen_AddOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_AddOp_0 = rewriter.create<::mlir::stablehlo::AddOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_AddOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:90
*/
struct GeneratedConvert1 : public ::mlir::RewritePattern {
  GeneratedConvert1(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.add", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::Attribute value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::AddOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
        ::mlir::Attribute arg1_0;
        if (!(!::mlir::failed(::mlir::success(::mlir::matchPattern(op1->getResult(0), ::mlir::m_Constant(&arg1_0)))))){
          return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
            diag << "::mlir::success(::mlir::matchPattern(op1->getResult(0), ::mlir::m_Constant(&arg1_0))) return ::mlir::failure";
          });
        }
        value = arg1_0;
        if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns1(rewriter, op1, arg1_0, "operand 0 of native code call '::mlir::success(::mlir::matchPattern($_self->getResult(0), ::mlir::m_Constant(&$0)))' failed to satisfy constraint: 'is int or float zero'"))) {
          return ::mlir::failure();
        }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:97
*/
struct GeneratedConvert2 : public ::mlir::RewritePattern {
  GeneratedConvert2(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.and", 2, context, {"stablehlo.and"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::AndOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::AndOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::AndOp tblgen_AndOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_AndOp_0 = rewriter.create<::mlir::stablehlo::AndOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_AndOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:100
*/
struct GeneratedConvert3 : public ::mlir::RewritePattern {
  GeneratedConvert3(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.and", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::stablehlo::ConstantOp zero;
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::AndOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_1(rewriter, op1, tblgen_ops, zero, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ zero.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:104
*/
struct GeneratedConvert4 : public ::mlir::RewritePattern {
  GeneratedConvert4(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.and", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::stablehlo::ConstantOp one;
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::AndOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_2(rewriter, op1, tblgen_ops, one, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:111
*/
struct GeneratedConvert5 : public ::mlir::RewritePattern {
  GeneratedConvert5(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.broadcast_in_dim", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::BroadcastInDimOp op;
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::BroadcastInDimOp>(op0); (void)castedOp0;
    op = castedOp0;
    operand = castedOp0.getODSOperands(0);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns4(rewriter, op0, tblgen_attr, "op 'stablehlo.broadcast_in_dim' attribute 'broadcast_dimensions' failed to satisfy constraint: 'is iota dimensions'"))) {
        return ::mlir::failure();
      }
      dims = tblgen_attr;
    }
    if (!(((*op.getODSResults(0).begin()).getType() == (*operand.begin()).getType()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op, operand' failed to satisfy constraint: 'operands are equal'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ operand }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:116
*/
struct GeneratedConvert6 : public ::mlir::RewritePattern {
  GeneratedConvert6(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.broadcast_in_dim", 2, context, {"stablehlo.broadcast_in_dim"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::mlir::DenseI64ArrayAttr dims_parent;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::BroadcastInDimOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::BroadcastInDimOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::BroadcastInDimOp type";
        });
      }
      operand = castedOp1.getODSOperands(0);
      {
        auto tblgen_attr = op1->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
        if (!(tblgen_attr)){
          return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
            diag << "expected op 'stablehlo.broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
          });
        }
        dims_parent = tblgen_attr;
      }
      tblgen_ops.push_back(op1);
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      dims = tblgen_attr;
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = getMergedBroadcastDimensions(rewriter, dims, dims_parent); (void)nativeVar_0;
    ::mlir::stablehlo::BroadcastInDimOp tblgen_BroadcastInDimOp_1;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*operand.begin()));
      if (auto tmpAttr = nativeVar_0) {
        tblgen_attrs.emplace_back(rewriter.getStringAttr("broadcast_dimensions"), tmpAttr);
      }
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_BroadcastInDimOp_1 = rewriter.create<::mlir::stablehlo::BroadcastInDimOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_BroadcastInDimOp_1.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:121
*/
struct GeneratedConvert7 : public ::mlir::RewritePattern {
  GeneratedConvert7(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.broadcast_in_dim", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::BroadcastInDimOp op;
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::BroadcastInDimOp>(op0); (void)castedOp0;
    op = castedOp0;
    operand = castedOp0.getODSOperands(0);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns5(rewriter, op0, tblgen_attr, "op 'stablehlo.broadcast_in_dim' attribute 'broadcast_dimensions' failed to satisfy constraint: 'is sorted dimensions'"))) {
        return ::mlir::failure();
      }
      dims = tblgen_attr;
    }
    if (!((llvm::cast<ShapedType>((*op.getODSResults(0).begin()).getType()).getNumElements() == llvm::cast<ShapedType>((*operand.begin()).getType()).getNumElements()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op, operand' failed to satisfy constraint: 'same number of elements'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = rewriter.create<stablehlo::ReshapeOp>(odsLoc, (*op.getODSResults(0).begin()).getType(), (*operand.begin())); (void)nativeVar_0;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ {nativeVar_0} }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:126
*/
struct GeneratedConvert8 : public ::mlir::RewritePattern {
  GeneratedConvert8(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.broadcast_in_dim", 1, context, {"stablehlo.transpose"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::BroadcastInDimOp op;
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::BroadcastInDimOp>(op0); (void)castedOp0;
    op = castedOp0;
    operand = castedOp0.getODSOperands(0);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      dims = tblgen_attr;
    }
    if (!((llvm::cast<ShapedType>((*op.getODSResults(0).begin()).getType()).getNumElements() == llvm::cast<ShapedType>((*operand.begin()).getType()).getNumElements()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op, operand' failed to satisfy constraint: 'same number of elements'";
      });
    }
    if (!((llvm::cast<ShapedType>((*op.getODSResults(0).begin()).getType()).getRank() == llvm::cast<ShapedType>((*operand.begin()).getType()).getRank()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op, operand' failed to satisfy constraint: 'same rank'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::TransposeOp tblgen_TransposeOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*operand.begin()));
      if (auto tmpAttr = dims) {
        tblgen_attrs.emplace_back(rewriter.getStringAttr("permutation"), tmpAttr);
      }
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_TransposeOp_0 = rewriter.create<::mlir::stablehlo::TransposeOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_TransposeOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:134
*/
struct GeneratedConvert9 : public ::mlir::RewritePattern {
  GeneratedConvert9(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.convert", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::ConvertOp convert;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::ConvertOp>(op0); (void)castedOp0;
    convert = castedOp0;
    operand = castedOp0.getODSOperands(0);
    if (!(((*convert.getODSResults(0).begin()).getType() == (*operand.begin()).getType()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'convert, operand' failed to satisfy constraint: 'operands are equal'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ operand }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:143
*/
struct GeneratedConvert10 : public ::mlir::RewritePattern {
  GeneratedConvert10(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.dynamic_broadcast_in_dim", 2, context, {"stablehlo.dynamic_broadcast_in_dim"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range shape(op0->getOperands());
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::mlir::DenseI64ArrayAttr dims_p;
    ::mlir::Operation::operand_range shape_p(op0->getOperands());
    ::mlir::DenseI64ArrayAttr expanding_p;
    ::mlir::DenseI64ArrayAttr nonexpanding_p;
    ::mlir::DenseI64ArrayAttr expanding;
    ::mlir::DenseI64ArrayAttr nonexpanding;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicBroadcastInDimOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicBroadcastInDimOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::DynamicBroadcastInDimOp type";
        });
      }
      operand = castedOp1.getODSOperands(0);
      shape_p = castedOp1.getODSOperands(1);
      {
        auto tblgen_attr = op1->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
        if (!(tblgen_attr)){
          return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
            diag << "expected op 'stablehlo.dynamic_broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
          });
        }
        dims_p = tblgen_attr;
      }
      {
        auto tblgen_attr = op1->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_expanding_dimensions");(void)tblgen_attr;
        expanding_p = tblgen_attr;
      }
      {
        auto tblgen_attr = op1->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_nonexpanding_dimensions");(void)tblgen_attr;
        nonexpanding_p = tblgen_attr;
      }
      tblgen_ops.push_back(op1);
    }
    shape = castedOp0.getODSOperands(1);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.dynamic_broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      dims = tblgen_attr;
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_expanding_dimensions");(void)tblgen_attr;
      expanding = tblgen_attr;
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_nonexpanding_dimensions");(void)tblgen_attr;
      nonexpanding = tblgen_attr;
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = getMergedBroadcastDimensions(rewriter, dims, dims_p); (void)nativeVar_0;
    auto nativeVar_1 = rewriter.getDenseI64ArrayAttr({}); (void)nativeVar_1;
    auto nativeVar_2 = rewriter.getDenseI64ArrayAttr({}); (void)nativeVar_2;
    ::mlir::stablehlo::DynamicBroadcastInDimOp tblgen_DynamicBroadcastInDimOp_3;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*operand.begin()));
      tblgen_values.push_back((*shape.begin()));
      if (auto tmpAttr = nativeVar_0) {
        tblgen_attrs.emplace_back(rewriter.getStringAttr("broadcast_dimensions"), tmpAttr);
      }
      if (auto tmpAttr = nativeVar_1) {
        tblgen_attrs.emplace_back(rewriter.getStringAttr("known_expanding_dimensions"), tmpAttr);
      }
      if (auto tmpAttr = nativeVar_2) {
        tblgen_attrs.emplace_back(rewriter.getStringAttr("known_nonexpanding_dimensions"), tmpAttr);
      }
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_DynamicBroadcastInDimOp_3 = rewriter.create<::mlir::stablehlo::DynamicBroadcastInDimOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_DynamicBroadcastInDimOp_3.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:152
*/
struct GeneratedConvert11 : public ::mlir::RewritePattern {
  GeneratedConvert11(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.dynamic_broadcast_in_dim", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::DynamicBroadcastInDimOp op;
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range shape(op0->getOperands());
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::mlir::DenseI64ArrayAttr expanding;
    ::mlir::DenseI64ArrayAttr nonexpanding;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicBroadcastInDimOp>(op0); (void)castedOp0;
    op = castedOp0;
    operand = castedOp0.getODSOperands(0);
    shape = castedOp0.getODSOperands(1);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.dynamic_broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      dims = tblgen_attr;
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_expanding_dimensions");(void)tblgen_attr;
      expanding = tblgen_attr;
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_nonexpanding_dimensions");(void)tblgen_attr;
      nonexpanding = tblgen_attr;
    }
    if (!((nonexpanding && cast<DenseI64ArrayAttr>(nonexpanding).size() == llvm::cast<ShapedType>((*op.getODSResults(0).begin()).getType()).getRank()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'nonexpanding, op' failed to satisfy constraint: 'all dims are non-expanding'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = rewriter.create<stablehlo::ConvertOp>(odsLoc, (*op.getODSResults(0).begin()).getType(), (*operand.begin())); (void)nativeVar_0;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ {nativeVar_0} }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:158
*/
struct GeneratedConvert12 : public ::mlir::RewritePattern {
  GeneratedConvert12(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.dynamic_broadcast_in_dim", 2, context, {"stablehlo.dynamic_reshape"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range shape(op0->getOperands());
    ::mlir::Operation::operand_range shape0(op0->getOperands());
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::mlir::DenseI64ArrayAttr expanding;
    ::mlir::DenseI64ArrayAttr nonexpanding;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicBroadcastInDimOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicReshapeOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::DynamicReshapeOp type";
        });
      }
      operand = castedOp1.getODSOperands(0);
      shape = castedOp1.getODSOperands(1);
      tblgen_ops.push_back(op1);
    }
    shape0 = castedOp0.getODSOperands(1);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("broadcast_dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.dynamic_broadcast_in_dim' to have attribute 'broadcast_dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      dims = tblgen_attr;
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_expanding_dimensions");(void)tblgen_attr;
      expanding = tblgen_attr;
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("known_nonexpanding_dimensions");(void)tblgen_attr;
      nonexpanding = tblgen_attr;
    }
    if (!(*shape.begin() == *shape0.begin())){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "Operands 'shape' and 'shape0' must be equal";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::DynamicReshapeOp tblgen_DynamicReshapeOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*operand.begin()));
      tblgen_values.push_back((*shape.begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_DynamicReshapeOp_0 = rewriter.create<::mlir::stablehlo::DynamicReshapeOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_DynamicReshapeOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:167
*/
struct GeneratedConvert13 : public ::mlir::RewritePattern {
  GeneratedConvert13(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.dynamic_reshape", 2, context, {"stablehlo.dynamic_reshape"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range shape(op0->getOperands());
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::mlir::Operation::operand_range shape_p(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicReshapeOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::DynamicReshapeOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::DynamicReshapeOp type";
        });
      }
      operand = castedOp1.getODSOperands(0);
      shape_p = castedOp1.getODSOperands(1);
      tblgen_ops.push_back(op1);
    }
    shape = castedOp0.getODSOperands(1);

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::DynamicReshapeOp tblgen_DynamicReshapeOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*operand.begin()));
      tblgen_values.push_back((*shape.begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_DynamicReshapeOp_0 = rewriter.create<::mlir::stablehlo::DynamicReshapeOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_DynamicReshapeOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:174
*/
struct GeneratedConvert14 : public ::mlir::RewritePattern {
  GeneratedConvert14(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.imag", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::ImagOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_3(rewriter, op1, tblgen_ops, lhs, rhs))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ rhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:181
*/
struct GeneratedConvert15 : public ::mlir::RewritePattern {
  GeneratedConvert15(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.maximum", 2, context, {"stablehlo.maximum"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::MaxOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::MaxOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::MaxOp tblgen_MaxOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_MaxOp_0 = rewriter.create<::mlir::stablehlo::MaxOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_MaxOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:187
*/
struct GeneratedConvert16 : public ::mlir::RewritePattern {
  GeneratedConvert16(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.minimum", 2, context, {"stablehlo.minimum"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::MinOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::MinOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::MinOp tblgen_MinOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_MinOp_0 = rewriter.create<::mlir::stablehlo::MinOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_MinOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:193
*/
struct GeneratedConvert17 : public ::mlir::RewritePattern {
  GeneratedConvert17(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.multiply", 2, context, {"stablehlo.multiply"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::MulOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::MulOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::MulOp tblgen_MulOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_MulOp_0 = rewriter.create<::mlir::stablehlo::MulOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_MulOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:197
*/
struct GeneratedConvert18 : public ::mlir::RewritePattern {
  GeneratedConvert18(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.multiply", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::stablehlo::ConstantOp zero;
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::MulOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_1(rewriter, op1, tblgen_ops, zero, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ zero.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:201
*/
struct GeneratedConvert19 : public ::mlir::RewritePattern {
  GeneratedConvert19(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.multiply", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::MulOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ConstantOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::ConstantOp type";
        });
      }
      {
        auto tblgen_attr = op1->getAttrOfType<::mlir::ElementsAttr>("value");(void)tblgen_attr;
        if (!(tblgen_attr)){
          return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
            diag << "expected op 'stablehlo.constant' to have attribute 'value' of type '::mlir::ElementsAttr'";
          });
        }
        if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns3(rewriter, op1, tblgen_attr, "op 'stablehlo.constant' attribute 'value' failed to satisfy constraint: 'is integer one'"))) {
          return ::mlir::failure();
        }
        value = tblgen_attr;
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:208
*/
struct GeneratedConvert20 : public ::mlir::RewritePattern {
  GeneratedConvert20(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.or", 2, context, {"stablehlo.or"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::OrOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::OrOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::OrOp tblgen_OrOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_OrOp_0 = rewriter.create<::mlir::stablehlo::OrOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_OrOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:211
*/
struct GeneratedConvert21 : public ::mlir::RewritePattern {
  GeneratedConvert21(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.or", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::stablehlo::ConstantOp one;
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::OrOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_2(rewriter, op1, tblgen_ops, one, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ one.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:215
*/
struct GeneratedConvert22 : public ::mlir::RewritePattern {
  GeneratedConvert22(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.or", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::stablehlo::ConstantOp zero;
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::OrOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_1(rewriter, op1, tblgen_ops, zero, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:222
*/
struct GeneratedConvert23 : public ::mlir::RewritePattern {
  GeneratedConvert23(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.real", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::RealOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_3(rewriter, op1, tblgen_ops, lhs, rhs))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:230
*/
struct GeneratedConvert24 : public ::mlir::RewritePattern {
  GeneratedConvert24(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.reduce", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range operands(op0->getOperands());
    ::mlir::Operation::operand_range init(op0->getOperands());
    ::mlir::DenseI64ArrayAttr dims;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::ReduceOp>(op0); (void)castedOp0;
    operands = castedOp0.getODSOperands(0);
    init = castedOp0.getODSOperands(1);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("dimensions");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.reduce' to have attribute 'dimensions' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns6(rewriter, op0, tblgen_attr, "op 'stablehlo.reduce' attribute 'dimensions' failed to satisfy constraint: 'is empty i64 array'"))) {
        return ::mlir::failure();
      }
      dims = tblgen_attr;
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ operands }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:237
*/
struct GeneratedConvert25 : public ::mlir::RewritePattern {
  GeneratedConvert25(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.reshape", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::ReshapeOp reshape;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::ReshapeOp>(op0); (void)castedOp0;
    reshape = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ReshapeOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::ReshapeOp type";
        });
      }
      operand = castedOp1.getODSOperands(0);
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = rewriter.create<stablehlo::ReshapeOp>(odsLoc, (*reshape.getODSResults(0).begin()).getType(), (*operand.begin())); (void)nativeVar_0;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ {nativeVar_0} }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:241
*/
struct GeneratedConvert26 : public ::mlir::RewritePattern {
  GeneratedConvert26(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.reshape", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::ReshapeOp reshape;
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::ReshapeOp>(op0); (void)castedOp0;
    reshape = castedOp0;
    operand = castedOp0.getODSOperands(0);
    if (!(((*reshape.getODSResults(0).begin()).getType() == (*operand.begin()).getType()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'reshape, operand' failed to satisfy constraint: 'operands are equal'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ operand }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:250
*/
struct GeneratedConvert27 : public ::mlir::RewritePattern {
  GeneratedConvert27(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.subtract", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range operand(op0->getOperands());
    ::mlir::Operation::operand_range operand0(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::SubtractOp>(op0); (void)castedOp0;
    if(::mlir::failed(__mlir_ods_local_type_constraint_StablehloAggressiveSimplificationPatterns1(rewriter, castedOp0, (*castedOp0.getODSOperands(0).begin()).getType(), "operand 0 of op 'stablehlo.subtract' failed to satisfy constraint: 'statically shaped tensor of any type values'"))) {
      return ::mlir::failure();
    }
    operand = castedOp0.getODSOperands(0);
    operand0 = castedOp0.getODSOperands(1);
    if (!(*operand.begin() == *operand0.begin())){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "Operands 'operand' and 'operand0' must be equal";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = ::mlir::stablehlo::getConstantLike(rewriter, odsLoc, 0, (*operand.begin())); (void)nativeVar_0;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ {nativeVar_0} }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:254
*/
struct GeneratedConvert28 : public ::mlir::RewritePattern {
  GeneratedConvert28(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.subtract", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::mlir::ElementsAttr value;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::SubtractOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto *op1 = (*castedOp0.getODSOperands(1).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 1 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::ConstantOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::ConstantOp type";
        });
      }
      {
        auto tblgen_attr = op1->getAttrOfType<::mlir::ElementsAttr>("value");(void)tblgen_attr;
        if (!(tblgen_attr)){
          return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
            diag << "expected op 'stablehlo.constant' to have attribute 'value' of type '::mlir::ElementsAttr'";
          });
        }
        if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns1(rewriter, op1, tblgen_attr, "op 'stablehlo.constant' attribute 'value' failed to satisfy constraint: 'is int or float zero'"))) {
          return ::mlir::failure();
        }
        value = tblgen_attr;
      }
      tblgen_ops.push_back(op1);
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:261
*/
struct GeneratedConvert29 : public ::mlir::RewritePattern {
  GeneratedConvert29(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.transpose", 1, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::DenseI64ArrayAttr dims;
    ::mlir::Operation::operand_range lhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::TransposeOp>(op0); (void)castedOp0;
    lhs = castedOp0.getODSOperands(0);
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::DenseI64ArrayAttr>("permutation");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.transpose' to have attribute 'permutation' of type '::mlir::DenseI64ArrayAttr'";
        });
      }
      if(::mlir::failed(__mlir_ods_local_attr_constraint_StablehloAggressiveSimplificationPatterns4(rewriter, op0, tblgen_attr, "op 'stablehlo.transpose' attribute 'permutation' failed to satisfy constraint: 'is iota dimensions'"))) {
        return ::mlir::failure();
      }
      dims = tblgen_attr;
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ lhs }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:268
*/
struct GeneratedConvert30 : public ::mlir::RewritePattern {
  GeneratedConvert30(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.get_tuple_element", 2, context, {}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::stablehlo::TupleOp tuple;
    ::mlir::Operation::operand_range operands(op0->getOperands());
    ::mlir::IntegerAttr idx;
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::GetTupleElementOp>(op0); (void)castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      auto castedOp1 = ::llvm::dyn_cast<::mlir::stablehlo::TupleOp>(op1); (void)castedOp1;
      if (!(castedOp1)){
        return rewriter.notifyMatchFailure(op1, [&](::mlir::Diagnostic &diag) {
          diag << "castedOp1 is not ::mlir::stablehlo::TupleOp type";
        });
      }
      tuple = castedOp1;
      operands = castedOp1.getODSOperands(0);
      tblgen_ops.push_back(op1);
    }
    {
      auto tblgen_attr = op0->getAttrOfType<::mlir::IntegerAttr>("index");(void)tblgen_attr;
      if (!(tblgen_attr)){
        return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
          diag << "expected op 'stablehlo.get_tuple_element' to have attribute 'index' of type '::mlir::IntegerAttr'";
        });
      }
      idx = tblgen_attr;
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    auto nativeVar_0 = (*tuple.getODSResults(0).begin()).getDefiningOp()->getOperand(idx.getInt()); (void)nativeVar_0;

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ {nativeVar_0} }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

/* Generated from:
    external/stablehlo/stablehlo/transforms/StablehloAggressiveSimplificationPatterns.td:275
*/
struct GeneratedConvert31 : public ::mlir::RewritePattern {
  GeneratedConvert31(::mlir::MLIRContext *context)
      : ::mlir::RewritePattern("stablehlo.xor", 2, context, {"stablehlo.xor"}) {}
  ::llvm::LogicalResult matchAndRewrite(::mlir::Operation *op0,
      ::mlir::PatternRewriter &rewriter) const override {
    // Variables for capturing values and attributes used while creating ops
    ::mlir::ElementsAttr value;
    ::mlir::stablehlo::XorOp op;
    ::mlir::stablehlo::ConstantOp lhs;
    ::mlir::Operation::operand_range rhs(op0->getOperands());
    ::llvm::SmallVector<::mlir::Operation *, 4> tblgen_ops;

    // Match
    tblgen_ops.push_back(op0);
    auto castedOp0 = ::llvm::dyn_cast<::mlir::stablehlo::XorOp>(op0); (void)castedOp0;
    op = castedOp0;
    {
      auto *op1 = (*castedOp0.getODSOperands(0).begin()).getDefiningOp();
      if (!(op1)){
        return rewriter.notifyMatchFailure(castedOp0, [&](::mlir::Diagnostic &diag) {
          diag << "There's no operation that defines operand 0 of castedOp0";
        });
      }
      if(::mlir::failed(static_dag_matcher_0(rewriter, op1, tblgen_ops, lhs, value))) {
        return ::mlir::failure();
      }
      tblgen_ops.push_back(op1);
    }
    rhs = castedOp0.getODSOperands(1);
    if (!((llvm::isa<BlockArgument>((*rhs.begin())) || !llvm::isa<stablehlo::ConstantOp>((*rhs.begin()).getDefiningOp())))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'rhs' failed to satisfy constraint: 'is not a constant.'";
      });
    }
    if (!(((*op.getODSResults(0).begin()).getDefiningOp()->hasTrait<hlo::OpTrait::IsCommutative>()))){
      return rewriter.notifyMatchFailure(op0, [&](::mlir::Diagnostic &diag) {
        diag << "entities 'op' failed to satisfy constraint: 'op is commutative'";
      });
    }

    // Rewrite
    auto odsLoc = rewriter.getFusedLoc({tblgen_ops[0]->getLoc(), tblgen_ops[1]->getLoc()}); (void)odsLoc;
    ::llvm::SmallVector<::mlir::Value, 4> tblgen_repl_values;
    ::mlir::stablehlo::XorOp tblgen_XorOp_0;
    {
      ::llvm::SmallVector<::mlir::Value, 4> tblgen_values; (void)tblgen_values;
      ::llvm::SmallVector<::mlir::NamedAttribute, 4> tblgen_attrs; (void)tblgen_attrs;
      tblgen_values.push_back((*rhs.begin()));
      tblgen_values.push_back((*lhs.getODSResults(0).begin()));
      ::llvm::SmallVector<::mlir::Type, 4> tblgen_types; (void)tblgen_types;
      for (auto v: castedOp0.getODSResults(0)) {
        tblgen_types.push_back(v.getType());
      }
      tblgen_XorOp_0 = rewriter.create<::mlir::stablehlo::XorOp>(odsLoc, tblgen_types, tblgen_values, tblgen_attrs);
    }

    for (auto v: ::llvm::SmallVector<::mlir::Value, 4>{ tblgen_XorOp_0.getODSResults(0) }) {
      tblgen_repl_values.push_back(v);
    }

    rewriter.replaceOp(op0, tblgen_repl_values);
    return ::mlir::success();
  }
};

void LLVM_ATTRIBUTE_UNUSED populateWithGenerated(::mlir::RewritePatternSet &patterns) {
  patterns.add<GeneratedConvert0>(patterns.getContext());
  patterns.add<GeneratedConvert1>(patterns.getContext());
  patterns.add<GeneratedConvert2>(patterns.getContext());
  patterns.add<GeneratedConvert3>(patterns.getContext());
  patterns.add<GeneratedConvert4>(patterns.getContext());
  patterns.add<GeneratedConvert5>(patterns.getContext());
  patterns.add<GeneratedConvert6>(patterns.getContext());
  patterns.add<GeneratedConvert7>(patterns.getContext());
  patterns.add<GeneratedConvert8>(patterns.getContext());
  patterns.add<GeneratedConvert9>(patterns.getContext());
  patterns.add<GeneratedConvert10>(patterns.getContext());
  patterns.add<GeneratedConvert11>(patterns.getContext());
  patterns.add<GeneratedConvert12>(patterns.getContext());
  patterns.add<GeneratedConvert13>(patterns.getContext());
  patterns.add<GeneratedConvert14>(patterns.getContext());
  patterns.add<GeneratedConvert15>(patterns.getContext());
  patterns.add<GeneratedConvert16>(patterns.getContext());
  patterns.add<GeneratedConvert17>(patterns.getContext());
  patterns.add<GeneratedConvert18>(patterns.getContext());
  patterns.add<GeneratedConvert19>(patterns.getContext());
  patterns.add<GeneratedConvert20>(patterns.getContext());
  patterns.add<GeneratedConvert21>(patterns.getContext());
  patterns.add<GeneratedConvert22>(patterns.getContext());
  patterns.add<GeneratedConvert23>(patterns.getContext());
  patterns.add<GeneratedConvert24>(patterns.getContext());
  patterns.add<GeneratedConvert25>(patterns.getContext());
  patterns.add<GeneratedConvert26>(patterns.getContext());
  patterns.add<GeneratedConvert27>(patterns.getContext());
  patterns.add<GeneratedConvert28>(patterns.getContext());
  patterns.add<GeneratedConvert29>(patterns.getContext());
  patterns.add<GeneratedConvert30>(patterns.getContext());
  patterns.add<GeneratedConvert31>(patterns.getContext());
}
