package Repository;
import domain.Identifiable;
import java.util.HashMap;
import java.util.Map;

public class MemoryRepository<T extends Identifiable,U> implements Repository.IRepository<T,U> {
    private Map<Integer, T> data = new HashMap<>();

    public void add(T elem) {
        if (elem != null && !data.containsKey(elem.getId())) {
            data.put(elem.getId(), elem);
        } else {
            throw new IllegalArgumentException("The entity is invalid .");
        }
    }


    public void update(T elem)
    {
        if (elem != null && data.containsKey(elem.getId())) {
            data.put(elem.getId(), elem);
        } else {
            throw new IllegalArgumentException("The entity not found or invalid.");
        }
    }



    public void remove(Integer id)
    {
        if (id != null) {
            T removedItem = data.remove(id);
            if (removedItem == null) {
                throw new IllegalArgumentException("The entity not found or invalid ID.");
            }
        }
    }


    public T findbyid(Integer id)
    {
        if (id != null) {
            return data.get(id);
        }
        return null;
    }


    public boolean exists(Integer id)
    {
        return data.containsKey(id);
    }


    public Iterable<T> getAll()
    {
        return data.values();
    }
}
