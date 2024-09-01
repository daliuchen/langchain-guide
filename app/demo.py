
if __name__ == '__main__':
    from langchain_core.runnables import RunnableParallel, RunnablePassthrough

    def inner_func(input):
        print(type(input))
        print("input",input)
        return input["num"]+10

    runnable = RunnableParallel(
        # 就是将原始的输入原封不动的放在这里
        passed=RunnablePassthrough(),
        # 这里修改了输入，所有的方法的input都是一个对象，是前一个对象的output
        modified=lambda x: x["num"] + 1,
        # 这里的意思是在原始的输入里面，在merge一个方法
        test = RunnablePassthrough.assign(**{"a1":inner_func})
    )

    res = runnable.invoke({"num": 1})
    print(res)