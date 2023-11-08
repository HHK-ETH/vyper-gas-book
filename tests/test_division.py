from ape import project


def test_optimized_division(deployer):
    optimized_contract = deployer.deploy(project.OptimizedDiv)

    c = optimized_contract.divide(10, 2)
    assert c == 5


def test_non_optimized_division(deployer):
    non_optimized_contract = deployer.deploy(project.NonOptimizedDiv)

    c = non_optimized_contract.divide(10, 2)
    assert c == 5
