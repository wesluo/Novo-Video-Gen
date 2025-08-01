# Architecture Decisions Log
## Multi-Product Video Generation System

*This document tracks all major architectural decisions for the evolution from single-product (Novo Insurance) to multi-product video script generation system.*

---

## Decision 1: Multi-Product Strategy Selection

**Date**: July 30, 2025  
**Status**: ✅ Approved for Implementation  
**Decision Maker**: User & Claude Code  

### Context
- Same development team managing 2-3 brands
- All brands focused on road safety but different products:
  - **Insurance**: Novo Insurance (current system)
  - **Crypto**: Cryptocurrency/blockchain product
  - **App**: Safety/driving mobile application
- Need to leverage existing story research and generation system

### Options Considered
1. **Complete Project Clone**: Separate isolated systems for each product
2. **Multi-Brand Generator**: Single system handling multiple brands with configuration

### Decision: Option 1 - Complete Project Clone

### Rationale
- **Different Product Messaging**: Insurance vs crypto vs app require fundamentally different brand messaging frameworks
- **Audience Differences**: Insurance buyers vs crypto traders vs app users have different motivations
- **Story Adaptation**: Same story needs completely different angles for each product
- **Risk Mitigation**: Prevents accidental brand message mixing
- **Team Isolation**: Allows product-specific experimentation without affecting others

### Rejected Alternative
Option 2 (Multi-Brand) rejected due to complexity of managing diverse product messaging in single system.

---

## Decision 2: Directory Structure Organization

**Date**: July 30, 2025  
**Status**: ✅ Approved for Implementation  
**Decision Maker**: User & Claude Code  

### Context
Need to organize multiple product systems within existing directory structure while maintaining shared resources.

### Decision: Product-Specific Folders with Shared Resources

### Structure
```
Novo Video Generation/
├── Insurance_Scripts/           # Current system (renamed from "Story Scripting")
├── Crypto_Scripts/             # New crypto product clone
├── App_Scripts/                # New app product clone  
├── Shared_Resources/           # Common assets
│   └── Story_Bank/            # Original research materials
├── README.md                  # Updated master documentation
└── ARCHITECTURE_DECISIONS.md  # This file
```

### Rationale
- **Isolation**: Each product gets independent workspace
- **Shared Research**: Common story research accessible to all products
- **Organization**: Clear separation while keeping everything in one location
- **Scalability**: Easy to add more products in future

---

## Decision 3: Story Management Strategy

**Date**: July 30, 2025  
**Status**: ✅ Approved for Implementation  
**Decision Maker**: User & Claude Code  

### Context
Each product needs different stories and messaging, but want to leverage existing story research.

### Decision: Clone First, Customize Later

### Implementation Plan
1. **Phase 1**: Create identical clones of all 90 stories across all products  
2. **Phase 2**: Wait for brand guidelines for crypto and app products
3. **Phase 3**: Customize stories, messaging, and themes per brand guidelines
4. **Phase 4**: Prune irrelevant stories and add product-specific stories

### Rationale
- **Functional Systems**: All products immediately operational  
- **Informed Customization**: Customize based on actual brand requirements
- **Iterative Approach**: Start working, refine based on experience
- **Risk Management**: Avoid premature optimization without brand input

---

## Decision 4: Cloning Methodology

**Date**: July 30, 2025  
**Status**: ✅ Approved for Implementation  
**Decision Maker**: User & Claude Code  

### Context
Need to create working copies of existing system for new products.

### Decision: Exact System Clones with Identical Initial State

### Implementation Details
- Copy all files: `story_database.json`, `script_generator.py`, `tracking_dashboard.py`, etc.
- Preserve all tracking data (7 completed scripts initially)
- Maintain same 90 stories with identical metadata
- Keep same brand messaging initially (Novo branding in all systems)

### Rationale
- **Immediate Functionality**: All systems work from day one
- **Known Good State**: Start from proven working system
- **Parallel Development**: Can customize each product independently
- **Rollback Safety**: Easy to revert changes if needed

---

## Next Steps & Future Decisions

### Pending Decisions
- [ ] **Brand Guidelines Integration**: Await specific branding guidelines for crypto and app products
- [ ] **Story Customization**: Determine which stories to keep/modify/add for each product
- [ ] **Messaging Framework**: Design brand-specific messaging systems
- [ ] **Theme Taxonomies**: Create product-specific theme categorizations

### Implementation Queue
1. Reorganize current system to Insurance_Scripts
2. Create Shared_Resources structure  
3. Clone systems for Crypto_Scripts and App_Scripts
4. Update master documentation
5. Await brand guidelines for customization phase

---

## Change Log

| Date | Change | Impact |
|------|--------|---------|
| 2025-07-30 | Initial architecture decisions documented | Established multi-product strategy |
| 2025-07-30 | Multi-product system implementation completed | 3 working systems created |
| 2025-07-30 | Documentation updated for multi-product context | All README/CLAUDE.md files reflect new structure |
| TBD | Brand guidelines received | Will trigger customization phase |
| TBD | Story customization completed | Product-specific content ready |

---

*This document will be updated as new architectural decisions are made during the multi-product system development.*