#include <string>
#include <exception>
#include <utility>

class Exceptions :public std::exception
{
protected:
	std::string message;
public:
	explicit Exceptions(std::string msg);
	const char* what() const noexcept override;

};

class RepoExceptions :public Exceptions
{
public:
	explicit RepoExceptions(std::string msg);
};