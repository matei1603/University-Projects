package Repository;
import domain.Identifiable;

public interface IRepository<T extends Identifiable,U> {
    void add(T elem);
    void update(T elem);
    void remove(Integer id);
    T findbyid(Integer id);
    boolean exists(Integer id);
    Iterable<T> getAll();
}
