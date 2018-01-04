# Data_Strcture_with_Python
## Chapter 1 绪论
本章讨论了一些与数据结构和算法有关的基础问题，包括：
1. 程序开发过程：
   - 分析阶段
   - 设计阶段
   - 编码阶段
   - 检查测试阶段
   - 测试/调试阶段
2. 问题求解：
   - 问题分析和严格化
   - 算法提出
   - 算法的精化和Python描述
3. 算法和算法分析
   - 问题和算法
   - 算法的代价及其度量
   - 算法分析
4. 数据结构
   - 数据结构及其分类：
     - 集合结构
     - 序列结构
     - 层次结构
     - 树形结构
     - 图结构
     
     
## Chapter 2 抽象数据和Python类
本章介绍了抽象数据类型（Abstract Data Type）的概念。
- 在程序开发实践中，人们逐渐认识到，仅有计算层面的抽象机制和抽象定义还不够，还需要考虑数据层面的抽象。能围绕一类数据建立程序组件，将该类数据的具体表示和相关操作的实现包装成一个整体，也是组织复杂程序的一种有效技术，可以用于开发各种有用的程序模块。
- 要把这种围绕着一类数据对象构造的模块做成数据抽象，同样需要区分模块的接口和实现。模块接口提供使用它提供的功能所需的所有信息，但不涉及具体实现细节，另一方面，模块实现者则要通过模块内部的一套数据定义和函数（过程）定义，实现模块接口所有的功能，从形式上和实际效果上满足模块接口的要求。
- 数据类型
  - 每种语言都提供了一组内置数据类型，为每个内置类型提供了一批操作（比如，整数的加减乘除等）。Python提供的基本类型包括：bool, int, float, str等。
  - 无论编程语言提供了多少内置类型，在处理复杂的问题时，程序员或早或晚都会遇到一些情况，此时，各种内置类型都不能满足或者不适合于自己的需要。在这种情况下，编程语言提供的组合类型有可能帮助解决一些问题。Python为数据的组合提供了 list, tuple, set, dict等结构（它们也可以看做是类型），编程时可以利用它们把一组相关数据组织在一起，构成一个数据对象，作为整体存储，传递和处理。
- 抽象数据类型：把对象的使用与其具体实现隔离开
  - 抽象数据类型的基本思想是把数据定义为抽象的对象集合，只为它们定义可用的个发操作，并不暴露其内部实现的具体细节，不论是其数据表示细节还是操作的实现细节。一个数据类型的操作通常可以分为三类：
    - 构造操作
    - 解析操作
    - 变动操作
  - 抽象数据类型的描述
    - 定义一个抽象数据类型，目的是要定义一类计算对象，它们具有某些特定的功能，可以在计算中使用。这类对象的功能体现为一组可以对它们使用的操作。当然，还需要为这一抽象数据类型确定一个类型名。
  - ADT是一种思想，也是一种组织程序的技术，主要包括：
    - 围绕着一类数据定义程序模块。
    - 模块的接口和实现分离。在ADT描述中，一般给出的是模块的接口规范，包括模块名，模块提供的各个操作的名字和参数。每个操作还有非形式化的语义说明。
    - 在需要实现时，从所用的编程语言里选一套合适的机制，采用合理的技术，实现这种ADT的功能，包括具体的数据表示和操作。

## Chaper 3 线性表
一个线性表是某类元素的一个集合，还记录着元素之间的一种顺序关系。它是最基本的数据结构之一，在实际程序中应用非常广泛，它还经常被用作更复杂的数据结构的实现基础。
-线性表的数学定义：集合 $E$ 上的一个线性表就是E中一组有穷个元素排成的序列 $L=(e_0, e_1,\cdots,e_{n-1})$,其中 $e_i\in E$ 且 $n\ge 0$。在这个表里可以包含 0 个或多个元素，序列中的每个元素在表里有一个确定的位置，成为该元素的**下标**。不包含任何元素的表称为**空表**。表元素之间存在着一个基本关系，称为**下一个关系**。对于表 $L$，其下一个关系是二元组的集合 $\{<e_0,e_1>, <e_1, e_2>, \cdots, <e_{n-2}, e_{n-1}>\}$。下一个关系是一种**顺序关系**,即**线性关系**。线性表是一种线性结构。
- 在一个非空的线性表里，存在着唯一的首元素和唯一的尾元素，除了首元素之外，表中每个元素都有且仅有一个前驱元素；除了尾元素之外的每个元素都有且仅有一个后继元素。
